import streamlit as st

def home():

    st.write('--------------------------------------------')
    st.markdown("<h1 style='text-align: center'>Topic Detection & Tracking</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center'>A system that allows you to scrape tweets from Twitter in a given period to detect and track the topics appearing in this period.</h5>", unsafe_allow_html=True)
    st.write(' ')

    st.markdown("<h4>Fonctionnalities:</h4>", unsafe_allow_html=True)
    st.markdown("1- Scraping data from news channels like CNN, FoxNews, BBC, ...")
    st.markdown("2- Tweets preporocessing")
    st.markdown("3- Topic detection")
    st.markdown("4- Topic tracking")

    st.markdown("<h6 style='text-align: center'>Made By: AKHADAM Ayoub & OULAHBIB Idriss</h6>", unsafe_allow_html=True)
    st.write('--------------------------------------------')