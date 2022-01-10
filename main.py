import streamlit as st

# import functions
from navbar import navbar
from home import home
from scrapData import scrapData
from textPreprocessing import textPreprocessing
from TopicDetection.topicDetection import topicDetection
from topicTracking import topicTracking

# RUN
st.set_page_config(page_title='Topic Detection', layout="wide")

menu_id = navbar()

if menu_id == 'Home':
    home()

elif menu_id == 'Scrape Data From Twitter':
    scrapData()

elif menu_id == 'Text Preprocessing':
    textPreprocessing()

elif menu_id == 'Topic Detection':
    topicDetection()



 

