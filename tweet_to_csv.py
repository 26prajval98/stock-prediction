import csv
import numpy as np
import tweepy
import pandas as pd
from textblob import TextBlob


def get_twitter_api():
	consumer_key = ''
	consumer_secret = ''

	auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
	api = tweepy.API(auth)
	return api

def get_tweet_score(date, api):
	score = 0
	n = 0
	for tweet in tweepy.Cursor(api.search, q="#ibm", count=100, lang="en", since="2017-04-03").items():
		score += TextBlob(tweet.text).sentiment.polarity
		n += 1

	if n > 0:
		score /= n
	else:
		score = np.random.random()
	return score
					

api = get_twitter_api()

with open('IBM.csv', 'r') as read_file:
	ibm_reader = csv.DictReader(read_file)

	field_names = ibm_reader.fieldnames
	field_names.append('Score')

	with open('IBM_with_twitterscore.csv', 'w') as write_file:
		ibm_writer = csv.DictWriter(write_file, fieldnames=field_names)

		ibm_writer.writeheader()

		for row in ibm_reader:
			date = row['Date']
			row['Score'] = get_tweet_score(date, api)
			ibm_writer.writerow(row)