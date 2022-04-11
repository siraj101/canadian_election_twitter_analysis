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


# Query by text search
# Setting variables to be used in format string command below
tweet_count = 10000
text_query = "#cdnpoli"
since_date = "2021-07-25"
until_date = "2021-09-20"

# Using OS library to call CLI commands in Python
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}" > text-query-tweets.json'.format(tweet_count, since_date, text_query, until_date))


# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df = pd.read_json('text-query-tweets.json', lines=True)

# Export dataframe into a CSV
tweets_df.to_csv('../data/tweets_election_df.csv', index=False)
print('done')