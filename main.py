import tweepy

client = tweepy.Client(bearer_token=BEARER_TOKEN)
query = '#elonmusk -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
for tweet in tweets.data:
    print(tweet.text)
