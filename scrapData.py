from datetime import datetime
import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st


def scrapFromTwitter(options_ticker, limit, since, until):
    list21=  options_ticker
    tweets_list1 = []
    for n, channel in enumerate(list21):
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{channel} since:{since} until:{until}').get_items()):
            if i>=limit: #number of tweets you want to scrape
                break

            tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.lang]) 

        tweets_df = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'lang'])
    
    
    return tweets_df
    

def scrapData() :
    list_search = ['CNN', 'FoxNews', 'BBCWorld', 'BNCNews', 'AJEnglish', 'RT_America']
    options_ticker = list()
   
    with st.form('Scraping section'):
        col1, col2 =  st.columns(2)
        with col1:
            options_ticker = st.multiselect(label='Select channel', options=list_search, default="CNN")
            since = st.date_input('Start date', key='input-since')
           
        with col2:
            limit = st.number_input('Number of tweets', min_value=1, max_value=10000, value=50)
            until = st.date_input('End date', key='input-until')
            

        submitted = st.form_submit_button('Scrap')

       

    if submitted: 
        with st.spinner("Scraping Data in progress ... "):
            df = scrapFromTwitter(options_ticker, limit, since, until)
            st.write(df)
        st.success(f'{df.shape[0]} tweets successfully loaded')

        # Download csv file
        csv = df.to_csv(index=False).encode('utf-8')

        dt = str(datetime.today()).replace('-', '.')
        dt = dt.replace(":", ".")
        dt = dt.replace(" ", "_")
        filename = f'{dt}_{"_".join(options_ticker)}.csv'
        
        st.download_button("Download csv", csv, filename, "text/csv",key='download-csv')