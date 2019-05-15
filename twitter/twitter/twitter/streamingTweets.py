from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv
import sys

class StdOutListener(StreamListener):

    # Define a function that is initialized when the miner is called
    def __init__(self, api=None):
        # That sets the
        self.api = api
        # Create a file with 'data_' and the current time
        self.filename = 'dataSets/'+'data' + '_' + time.strftime('%Y%m%d-%H%M%S') + '.csv'
        # Create a new file with that filename
        csv_file = open(self.filename, 'w')

        # Create a csv writer
        csv_writer = csv.writer(csv_file)

        # Write a single row with the headers of the columns

    # When a tweet appears
    def on_status(self, status):

        # Open the csv file created previously
        csv_file = open(self.filename, 'a')

        # Create a csv writer
        csv_writer = csv.writer(csv_file)

        # If the tweet is not a retweet
        if not 'RT @' in status.text:
            # Try to
            try:
                if status.is_quote_status:
                    text = [status.extended_tweet['full_text']]
                else:
                    text = [status.text]
                csv_writer.writerow(text)
            except Exception:
                pass

        # Close the csv file
        csv_file.close()

        # Return nothing
        return

    # When an error occurs
    def on_error(self, status_code):
        # Print the error code
        print('Encountered error with status code:', status_code)

        # If the error code is 401, which is the error for bad credentials
        if status_code == 401:
            # End the stream
            return False

    # When a deleted tweet appears
    def on_delete(self, status_id, user_id):

        # Print message
        print("Delete notice")

        # Return nothing
        return

    # When reach the rate limit
    def on_limit(self, track):

        # Print rate limiting error
        print("Rate limited, continuing")

        # Continue mining tweets
        return True

    # When timed out
    def on_timeout(self):

        # Print timeout message
        print(sys.stderr, 'Timeout...')

        # Wait 10 seconds
        time.sleep(10)

        # Return nothing
        return


# Create a mining function
def start_mining(queries):

    # Inputs list of strings. Returns tweets containing those strings.

    # Variables that contains the user credentials to access Twitter API
    consumer_key = "87r1JNrML8mQznIAHTApW0vwZ"
    consumer_secret = "366miuotXwhLstzY2GRmRjMptQXgMkn6bMfYEwKYu8zhTQPSKn"
    access_token = "303277563-oWBveWeoA0lSPXNUrrwlGWWhHccfqQAdfBNbkx7C"
    access_token_secret = "6OYHXM3eF4sbqEUQXyzULEi4yrYdwC54WBrc6EiQstXKO"

    # Create a listener
    listener = StdOutListener()

    # Create authorization info
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create a stream object with listener and authorization
    stream = Stream(auth, listener, tweet_mode='extended')

    # Run the stream object using the user defined queries
    stream.filter(track=queries)

    return listener.filename


def stream_tweets(hash_tag):
    tweets_file = unicode(start_mining(hash_tag).strip(codecs.BOM_UTF8), 'utf-8')
    return tweets_file


#stream_tweets(["#BoycottChineseProducts"])
