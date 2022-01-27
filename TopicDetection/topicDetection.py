import streamlit as st
import pandas as pd

from TopicDetection.iterative_method import iterative_method
from TopicDetection.sidebar import sidebar
from TopicDetection.lda_params import *
from TopicDetection.single_iteration_method import single_iteration_method

def topicDetection():
    # Sidebar
    sidebar()

    # Upload the clean dataset
    st.subheader('Upload the clean data')
    dataset = st.file_uploader("", type = ['csv'])
    if dataset is not None:
        tweets = pd.read_csv(dataset)

        single_iteration_method(tweets)

        iterative_method(tweets)
    
            

            






        
                



    

