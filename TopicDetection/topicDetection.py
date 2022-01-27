from tracemalloc import start
from matplotlib.pyplot import step
import streamlit as st
import pandas as pd
from TopicDetection.sidebar import sidebar
from TopicDetection.lda_params import *
from TopicDetection.topic_visualization import topic_visualization
from TopicDetection.train_lda import *
from streamlit import components

def topicDetection():
    # Sidebar
    sidebar()

    # Upload the clean dataset
    st.subheader('Upload the clean data')
    dataset = st.file_uploader("", type = ['csv'])
    if dataset is not None:
        tweets = pd.read_csv(dataset)

        # Train the LDA model
        st.subheader('Train LDA Model')
        with st.form('lda'):
            parametres = get_lda_params()
            submitted = st.form_submit_button('Train')
        
        if submitted:
            with st.spinner("Training LDA model in progress ... "):
                    id2word, corpus, lda_model = train_lda(tweets,parametres)
        

            # LDA Results
            topics = lda_model.show_topics(formatted=False, num_words=50,num_topics=parametres['num_topics'], log=False)
            get_lda_results(topics)
            
            
            # LDA Evaluation
            with st.spinner('Calculating coherence metric'):
                data = tweets.clean_tweet.values.tolist()
                data_words = list(sent_to_words(data))
                coherence = calculate_coherence(lda_model, data_words, id2word, 'c_v')
                with st.expander('LDA Evaluation metric'):
                    st.write('Coherence')
                    st.write(coherence)

            # Pyldavis 
            with st.spinner('Preparing visualization'):
                #st.subheader('Topics visualization')
                with st.expander('Topics visualization'):
                    html = topic_visualization(lda_model, corpus, id2word)
                    components.v1.html(html, width=1300, height=800)


    
            

            






        
                



    

