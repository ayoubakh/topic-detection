import streamlit as st
from DataScraper import DataScraper
from DataPreProcessor import DataPreProcessor

## Data Scrapping
channels = ['CNN', 'FoxNews', 'BBCWorld']
start_date = '2021-12-13'
end_date = '2021-12-14'
count = 50

ds = DataScraper(channels, start_date, end_date, count)
ds.start()


## Data preprocessing
# data = ""
# datapreprocessor = DataPreProcessor(data)
# clean_data = datapreprocessor.start()


