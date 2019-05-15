from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import collections

activities = ['Positive Tweets', 'Negative Tweets', 'Neutral Tweets']


def bar_chart(sentiment_count):
    sentiment_count = collections.OrderedDict(sorted(sentiment_count.items()))
    activity = sentiment_count.keys()
    count = sentiment_count.values()
    y_pos = np.arange(len(activity))
    plt.barh(y_pos, count, color="red", align='center', alpha=0.5)
    plt.yticks(y_pos, activity)
    plt.xlabel('NUMBER OF WORDS')
    plt.ylabel('POLARITY OF WORD')
    plt.show()


def pie_chart(sentiment_count):
    del sentiment_count["total_tweets"]
    plt.pie(sentiment_count.values(), labels=sentiment_count.keys(), startangle=90, autopct='%.1f%%')
    plt.show()


def word_cloud(words):
    cloud = WordCloud().generate(words)
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def print_count(sentiment_count):
    print('Number Of Positive Tweets: ' + str(sentiment_count["positive_tweets"]))
    print('Number Of Negative Tweets: ' + str(sentiment_count["negative_tweets"]))
    print('Number Of Neutral Tweets: ' + str(sentiment_count["neutral_tweets"]))

