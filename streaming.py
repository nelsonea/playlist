#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2980842884-brfYZGmyLnZTIKX8vA15aOEBAZ7l7fdFsENcXL1"
access_token_secret = "M49I3yCLHexaDxDttfyT7AXD2BmHyLFjEsSX9JSfrntVm"
consumer_key = "iybXUDyKSn4sW497xzMWZ5LzP"
consumer_secret = "9K2Faf6Eo2rlH7GvMrcty4kM2FoFrSdoHvpW34avGw0QEjqwvN"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the location of lower Manhattan
stream.filter(track=['#NowPlaying'])
