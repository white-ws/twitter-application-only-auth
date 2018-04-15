from twitter_oauth.app_only import AppOnlyAuth
import os
import requests

API_TWEET_SEARCH = 'https://api.twitter.com/1.1/search/tweets.json'

class TwitterApi:
	def __init__(self, consumer_key, consumer_secret):
		auth = AppOnlyAuth(consumer_key, consumer_secret)
		self.access_token = auth.get_access_token()

	def search_tweet_from_user(self, user):
		headers = {
			'Authorization': 'Bearer {}'.format(self.access_token)
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