from twitter import twitter as twitter
from db  import mongo

docs = twitter.call_search ("Petro") ["results"]
#print(docs)
#if 'results' in docs:
mongo.save_many(docs)













