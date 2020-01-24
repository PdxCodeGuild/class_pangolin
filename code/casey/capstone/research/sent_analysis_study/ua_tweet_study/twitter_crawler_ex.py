import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'zIBVTTzH7JJECyk13IX4NhEwA'
consumer_secret = 'LNXB9EvF17aGWbdqlXUvd5T4VnEGyL2jXVgeQh3YCAtUE54Fw9'
access_token = '1218694128260640768-8htRlFCLm99PMtvhJYFwJSR0GhvNwD'
access_token_secret = 'dNaoB8ZMRs8OiI8XCB0BACcJu4wgqH5enmzLbYY0TC5AS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####Beatles
# Open/Create a file to append data
csvFile = open('beatles.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#beatles",count=100,
                           lang="en",
                           since="2020-01-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])