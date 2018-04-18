from auth.oauth2 import AppOnlyAuth
import os
import requests

API_TWEET_SEARCH = 'https://api.twitter.com/1.1/search/tweets.json'

class TwitterApi:
	def __init__(self, consumer_key, consumer_secret):
		self.auth = AppOnlyAuth(consumer_key, consumer_secret)

	def search_tweet_from_user(self, user):
		headers = {
			'Authorization': self.auth.get_authorization()
		}
		params = {
			'q': 'from:{}'.format(user),
			'count':'1'
		}
		url = API_TWEET_SEARCH

		response = requests.get(url, params = params, headers = headers)

		if response.status_code != requests.codes.ok:
			raise Exception('Invalid credentials')

		return response.json()
