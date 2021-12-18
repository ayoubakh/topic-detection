import streamlit as st
from DataScraper import DataScraper
from DataPreProcessor import DataPreProcessor
from navbar import navbar

## Data Scrapping
channels = ['CNN', 'FoxNews', 'BBCWorld']
start_date = '2021-12-13'
end_date = '2021-12-14'
count = 500

#ds = DataScraper(channels, start_date, end_date, count)
#ds.start()


## Data preprocessing
# data = ""
# datapreprocessor = DataPreProcessor(data)
# clean_data = datapreprocessor.start()

# RUN
st.set_page_config(page_title='TDT', layout="wide")
menu_id = navbar()
if menu_id == 'Home':
    st.write('--------------------------------------------')
    #st.write('# Topic Detection & Tracking')
    st.markdown("<h1 style='text-align: center'>Topic Detection & Tracking</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center'>A system that allows us to scrape tweets from Twitter in a given period to detect and track the topics appearing in this period.</h5>", unsafe_allow_html=True)
    st.write(' ')
    st.markdown("<h6 style='text-align: center'>Made By: AKHADAM Ayoub & OULAHBIB Idriss</h6>", unsafe_allow_html=True)
    st.write('--------------------------------------------')

elif menu_id == 'Scrape Data From Twitter':
    st.write('scraping here')

elif menu_id == 'Topic Detection':
    st.write('detection here')

elif menu_id == 'Topic Tracking':
    st.write('tracking here')


 



