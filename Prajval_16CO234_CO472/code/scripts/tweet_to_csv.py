import csv
import numpy as np
import tweepy
import pandas as pd
from textblob import TextBlob
import datetime

def date_and_next_date(date):
	date_obj = datetime.datetime.strptime(date, '%d-%m-%Y')
	next_date_obj = date_obj + datetime.timedelta(days=-1)
	date = date_obj.strftime("%Y-%m-%d")
	next_date = next_date_obj.strftime("%Y-%m-%d")
	date, next_date = next_date, date
	return date, next_date

def get_twitter_api():
	# Add consumer key and secret
	consumer_key = ''
	consumer_secret = ''

	auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
	api = tweepy.API(auth)
	return api

def get_tweet_score(d, api):
	score = 0
	n = 0
	date, next_date = date_and_next_date(d)
	for tweet in tweepy.Cursor(api.search, q="#ibm", count=100, lang="en", since=date, until=next_date).items():
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