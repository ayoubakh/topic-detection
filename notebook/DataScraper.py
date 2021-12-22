""" 
Data Scrapping using snscrap 

"""

import enum
from pandas._config.config import options
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime
import os
import streamlit as st

class DataScraper:

    """
    A class used to scrap data using snscrap

    ...

    Attributes
    ----------
    channles : list
        a list of channels that we want to scrap data from
    start_date : date
        start date
    start_date : date
        end date
    count : integer
        number of tweets you want o scrap
    dest_dir : int
        the destination directory of the scraped data

    Methods
    -------
    scrap(self, channel, start_date, end_date)
        scrap data from a given channel between the start_date and the end_date
    write(self, df):
        writing scrapped data in a csv file
    start(self):
        start scarping 
    """
    
    def __init__(self, channels, start_date, end_date, count=700, destdir="./data"):
        self.channels = channels
        self.destdir = destdir
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        dt = str(datetime.today()).replace('-', '.')
        dt = dt.replace(":", ".")
        self.filename = f'{dt}_{"_".join(channels)}.csv'
    
    def scrap(self, channel, start_date, end_date):
        tweets_list1 = []
        
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{channel} since:{start_date} until:{end_date}').get_items()):
            if i>self.count:
                break
            #declare the attributes to be returned
            tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.lang]) 

        # Creating a dataframe from the tweets list above 
        # return pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'lang'])
        #twwets_df = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'lang'])
    
    def write(self, df):
        file = f'{self.destdir}/{self.filename}'
        print(f"writing data file {file}")
        mode="w"
        if os.path.isfile(file) :
            mode = 'a'
        df.to_csv(f"{self.destdir}/{self.filename}", index=False, mode = mode)
        pass
    
    def start(self):
        for channel in self.channels:
            print(f"scrapping data from:{channel}")
            tweets = self.scrap(channel, self.start_date, self.end_date)
            self.write(tweets)
        pass



def scrapFromTwitter(options_ticker):
    list21=  options_ticker
    tweets_list1 = []
    for n, k in enumerate(list21):
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{k}').get_items()):
            print(str(i)+ " | "+k+" | "+ str(tweet.date))
            tweets_list1.append([k, tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.lang]) 
            tweets_df = pd.DataFrame(tweets_list1, columns=['Search','Datetime', 'Tweet Id', 'Text', 'Username', 'lang'])
    
    print('list of tweets created')
    return tweets_df
    


def scrapData() :
    op = st.checkbox('add more channels for search')
    list_search = ['CNN', 'FoxNews', 'BBCWorld']
    options_ticker = list()
    if not op:
        with st.form('Scrapinf section'):
            col1, col2, col3 = st.columns((2, 2, 2))
            with col1:
                options_ticker = st.multiselect(label='Select channel', options=list_search, default="CNN")
                submitted = st.form_submit_button('Scrap')

        if submitted:
            st.spinner("Loading Data in progress ... ")
            df = scrapFromTwitter(options_ticker)
            st.success(f'{df.shape[0]} tweets successfully loaded')
            # downloadData(df)
    else:
        pass



