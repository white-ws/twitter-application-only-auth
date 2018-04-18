# Twitter Application-Only Authentication For Python

A simple implementation of Twitter's Application-Only Authentication (OAuth2 with Client Credentials) in Python, along side with a Twitter API Wrapper for searching newest tweet from an account.

Tested with Python 3.6.0

# Usage

Using Twitter Api Wrapper with app-only auth to get newest tweet from an account

```python
from twitter_wrapper import TwitterApi
import json

consumer_key = 'xvz1evFS4wEEPTGEFPHBog'
consumer_secret = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg'


twitter = TwitterApi(consumer_key, consumer_secret)
response = twitter.search_tweet_from_user('TEDTalks')

print(json.dumps(response, indent=4))

```

Using the app-only auth with your own Twitter REST API call request

```python
from twitter_oauth.app_only import AppOnlyAuth
import requests
import json

consumer_key = 'xvz1evFS4wEEPTGEFPHBog'
consumer_secret = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg'


auth = AppOnlyAuth(consumer_key, consumer_secret)
access_token = auth.get_access_token()

header = {
	'Authorization': 'Bearer {}'.format(access_token)
	}

response = requests.get('https://api.twitter.com/1.1/trends/available.json', headers = header)
if response.status_code != requests.codes.ok:
	raise Exception('Invalid credentials')


response_body = response.json()

print(json.dumps(response_body, indent=4))
```

You can find your App consumer key & secret in https://apps.twitter.com/.      
After finishing the registration & configuration, go to your Application detail page and check out `Keys and Access Token` tab.
