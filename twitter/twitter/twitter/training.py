from nltk.classify import NaiveBayesClassifier
import pandas as pd


def word_feats(words):
    return dict([(word, True) for word in words])


def get_data_set(train_file, data_set):
    data_frame = pd.read_csv(train_file)
    for data in data_frame.itertuples():
        data_set = data_set + [(word_feats(data[1]), data[2])]
    return data_set


train_data_set = []
train_data_set = get_data_set("twitter/trainSets/emoji.csv", train_data_set)
train_data_set = get_data_set("twitter/trainSets/Negative Words.csv", train_data_set)
train_data_set = get_data_set("twitter/trainSets/Neutral Words.csv", train_data_set)
train_data_set = get_data_set("twitter/trainSets/Positive Words.csv", train_data_set)


def train():
    classifier = NaiveBayesClassifier.train(train_data_set)
    return classifier
