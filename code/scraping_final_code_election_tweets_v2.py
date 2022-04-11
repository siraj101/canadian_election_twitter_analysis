# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:09:44 2022

@author: Mehdi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:53:59 2022

@author: Mehdi
"""




import os
import pandas as pd
from datetime import datetime, timedelta


# Query by text search
# Setting variables to be used in format string command below

tweet_count = 500 #tweets per day
text_query = "#cdnpoli"
since_date = "2021-07-01"
until_date = "2021-09-20"



dtformat = '%Y-%m-%d'  # Setting the date format required by twitter API

def time_slots(mydate, days):
    date = datetime.strptime(mydate, dtformat)
    new_date = date - timedelta(days=days)
    return new_date.strftime(dtformat)

#test
time_slots(since_date,1)


n_days = 30 #number of days we're looking into 
df = pd.DataFrame()

for i in range(n_days):
    
    # Using OS library to call CLI commands in Python
    os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}" > text-query-tweets.json'.format(tweet_count, since_date, text_query, until_date))

    # Reads the json generated from the CLI command above and creates a pandas dataframe
    tweets_df = pd.read_json('text-query-tweets.json', lines=True)
    
    #append to final dataframe
    df = df.append(tweets_df, ignore_index=True)
    
    #Moving back by 1 day
    until_date = time_slots(until_date,1)


# Export dataframe into a CSV
df.to_csv('C:/Users/Mehdi/Desktop/tweets_election_df_v2.csv', index=False)

