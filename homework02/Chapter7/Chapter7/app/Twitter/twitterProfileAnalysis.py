import sys
import csv
import tweepy as tw
import pandas as pd
import collections
from re import findall
from sys import argv, exit
from urllib.request import urlopen
from twitter_scraper import Profile

user_name = "buzkiran44"

consumer_key = "GJDW8sTnCvfKa2MIWs2eG00LH"
consumer_secret = "CP2W3MyhX1GTHmlef2Vp1GHvL8alZ7sqJRWBncwPiS04aHRv7M"
access_key = "1289378270732050432-0IXbBqlFTQ0rT8IHJtdCE1Cxr55HXi"
access_secret = "W3XMNVyTEOpRLnjbLNocqEwhrnjd6HaxYqQK593kW4R4J"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tw.API(auth)

def get_tweets(username):
    number_of_tweets = 1000 

    tweets_for_csv = []
    tweets_to_count = []

    for tweet in tw.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
        tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
        tweets_to_count.append(tweet.text.split())

    concat_words = [j for i in tweets_to_count for j in i]
    lower_case = [word.lower() for word in concat_words]
    counts_lower_case = collections.Counter(lower_case)
    counts_lower_case_pd = pd.DataFrame(counts_lower_case.most_common(25), columns=['words', 'count'])

    print(counts_lower_case_pd)

    outfile = username + "_tweets.csv"

    with open(outfile, 'w+') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(tweets_for_csv)

get_tweets(user_name)