import tweepy
from textblob import TextBlob

consumer_key = 'Z0bEpYrdrA91bIqFhHIUN78Oz'
consumer_secret = 'g5AudmBzHv1Y9eAjixXtV91TrgtCpX6NExb2QhNTV1fH3QAGcj'

access_token = '957223669738045440-NI42JKqdmyN7HinPszkBQzev4L1It9n'
access_token_secret = 'aGoJRuSkDguVnoSQ6SR87eVPcou5BcgR6gLdnwkS547n8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Virat')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
