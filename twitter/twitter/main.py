from twitter import training as training
from twitter import classify as classify
from twitter import view as view
from twitter import streamingTweets as streamingTweets
import time

def initialize():
    return training.train()


def analysis(classifier, data_frame, hash_tag=None, tweets_file='/home/mrudula/project_8th_sem/python_3_env_00/lib/python2.7/sentiment_analysis/twitter/twitter/test_case1.csv'):
    if hash_tag:
        tweets_file = streamingTweets.stream_tweets(hash_tag)
    sentiment_count, words, word_count = classify.data(classifier, tweets_file, data_frame)
    #view.bar_chart(word_count)
    #view.pie_chart(sentiment_count)
    #view.word_cloud(words)
    #view.print_count(sentiment_count)


if __name__ == "__main__":
    classifier = initialize()
    frame = classify.classify_feature_set()
    start_time = time.time()
    analysis(classifier, frame)
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
