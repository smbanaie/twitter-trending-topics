# -*- coding: utf-8 -*-import twitter_config

from birdy.twitter import  StreamClient,Str
import twitter_config


CONSUMER_KEY = twitter_config.consumer_key
CONSUMER_SECRET = twitter_config.consumer_secret
access_token = twitter_config.access_token
access_secret = twitter_config.access_secret

# client = AppClient(CONSUMER_KEY, CONSUMER_SECRET)
# access_token = client.get_access_token()


class TweetListener(StreamListener):
	# def __init__(self):
		# self.client = pykafka.KafkaClient("localhost:9092")
		# self.producer = self.client.topics[bytes('twitter','utf-8')].get_producer()

	def on_data(self, data):
		try:
			print(""+data)
			json_data = json.loads(data)
			words = json_data['text'].split()

			ls = list(filter(lambda x: x.lower().startswith('#'), words))
			if(len(ls)!=0):
				for word in ls:
					print(word)
					# self.producer.produce(bytes(word,'utf-8'))
			return True
		except KeyError:
			print ("Exceptipn")
			return True

	def on_error(self, status):
		print(status)
		return True

client = StreamClient(CONSUMER_KEY, CONSUMER_SECRET, access_token,access_secret)


response = client.stream.statuses.filter.post(languages=['fa'],track=['با'])
for data in response.stream():
    print (data)