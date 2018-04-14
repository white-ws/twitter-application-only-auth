import oauth2 as oauth
import base64
import requests
import time
import os

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')

def get_encoded_credentials(consumer_key, consumer_secret):
	bearer_token_credentials = "{}:{}".format(consumer_key, consumer_secret)
	return base64.b64encode(bearer_token_credentials.encode('utf-8')).decode('utf-8')

# print(get_encoded_token(consumer_key, consumer_secret))
client_credentials = get_encoded_credentials(consumer_key, consumer_secret)
for i in range(0, 1):
	r = requests.post("https://discordapp.com/api/webhooks/408500870762856448/0ZrHuLDKldfNo_e50tFJhYmrdww9zP7vxhXgOGHwDZvjtlhoBaoRpu2zHkrPTGxfz8o0", data = {'content':'I\'m the God? <:DartAAAAAnyan:411894112250232832>'})
	time.sleep(1)

# def request_bearer_token(client_credentials):
