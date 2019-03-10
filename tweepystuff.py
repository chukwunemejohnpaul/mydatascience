import tweepy
from textblob import TextBlob
consumerkey = "ivUf9xcLrtuCSZ12dqdI1ASVK"
consumersecret = "3z6oXGhsHBLCPkMHAl9wjOF0VaRO0oe3DkKiknPIAc3xNKNl9J"
accesstoken = "987053000089882631-jfQLibVeo1ErvM1FeA2hLyQlCEp8ipT"
accesstokensecret = "ZjWLk2WBo5y5Ctv9ZkGEtQtbV85Qex4AcPsmNBoN3hvvR"
auth = tweepy.OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesstoken,accesstokensecret)
api = tweepy.API(auth)
public_tweets = api.search("donald trump")
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)