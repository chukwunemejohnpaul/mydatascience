import tweepy
from textblob import TextBlob
consumerkey = "your_secret"
consumersecret = "your_secret"
accesstoken = "your_secret"
accesstokensecret = "your_secret"
auth = tweepy.OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesstoken,accesstokensecret)
api = tweepy.API(auth)
public_tweets = api.search("donald trump")
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
