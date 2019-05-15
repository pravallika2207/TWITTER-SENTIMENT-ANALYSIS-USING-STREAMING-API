from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import emoji
import pandas as pd
import glob

tokenizer = RegexpTokenizer(r'\w+')
stopWords = set(stopwords.words('english'))
wnl = WordNetLemmatizer()


def word_feats(words):
    return dict([(word, True) for word in words])


def classify_feature_set():
    path = r'/home/mrudula/project_8th_sem/python_3_env_00/lib/python2.7/sentiment_analysis/twitter/twitter/trainSets'
    filenames = glob.glob(path + "/*.csv")
    df = []
    for file in filenames:
        data_frame = pd.read_csv(file, index_col=None, header=0)
        df.append(data_frame)
        print(file)
    frame = pd.concat(df, axis=0, ignore_index=True)
    return frame


def get(word, data_frame):
    data = data_frame[data_frame['token'] == word]
    p = data['polarity'].tolist()
    if p:
        polarity = p[0]
        return polarity
    return 99


def data(classifier, tweets_file, frame):
    count = {"positive_tweets": 0, "negative_tweets": 0, "neutral_tweets": 0, "total_tweets": 0}
    positive_threshold = 2
    negative_threshold = -2
    all_words = ''
    # get file dynamically
    data_frame = pd.read_csv(tweets_file, low_memory=False)
    count["total_tweets"] = len(data_frame)
    word_count = {-10: 0, -9: 0, -8: 0, -7: 0, -6: 0, -5: 0, -4: 0, -3: 0, -2: 0, -1: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for data in data_frame.itertuples():
        data = emoji.demojize(unicode(data[1], "utf-8"), delimiters=(" ", " "))
        data = re.sub(r'\d+', '', data)
        data = data.lower()
        words = tokenizer.tokenize(data)
        words_filtered = []

        for word in words:
            if word not in stopWords:
                word = wnl.lemmatize(word)
                words_filtered.append(word)
                all_words = all_words + word + ' '
                neg = 0
                pos = 0

        for word in words_filtered:
            class_result = get(word, frame)
            if class_result == 99:
                continue
                class_result = classifier.classify(word_feats(word))
            if class_result < 0:
                neg = neg + class_result
            if class_result > 0:
                pos = pos + class_result
            word_count[class_result] += 1
        polarity = float(pos+neg)/len(words_filtered)

        if polarity >= positive_threshold:
            count["positive_tweets"] += 1
        elif polarity <= negative_threshold:
            count["negative_tweets"] += 1
        else:
            count["neutral_tweets"] += 1
    return count, all_words, word_count
