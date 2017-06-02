# encoding: utf-8
from TwitterSearch import * 
import subprocess
try:
    f = open("/Users/ethantien/Documents/hackathons/hackGSU/companies.txt", "r+")
    firstLine = f.readlines()[0]

    #subprocess.call("python3 meow.py", shell=True)

    companies = firstLine.split(", ")

    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
     # let's define all words we would like to have a look for
    tso.set_language('en') # language
    tso.set_include_entities(False) # and don't give us all those entity information
    tweets = [];

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '2utN8sjAUlmCgbYsRqV2Tei7F',
        consumer_secret = 'ZVtyJBYcjLYEBybMwL3lroEHs0jFIVxNm9jQwiTFDIhe0TJDWq',
        access_token = '526584139-MgB543wP45ds6hADNAivTw9AZwrcZl9ABwrv7Qml',
        access_token_secret = 'fGPW3Q0KNMoNONe8XbPSLlk8pSU7XPyaAzmalzpI6lmft'
    )
    #print(ts.VerifyCredentials())

     # this is where the fun actually starts :)
    for ele in companies:
        tso.set_keywords([ele])
        for tweet in ts.search_tweets_iterable(tso):
            #print(tweet['text'].encode('ascii', 'ignore'));
            tweets.append( '%s' % (tweet['text'].encode('utf-8')) )
    #for ele in tweets:

        #pass to neural net
        #print (ele)

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)