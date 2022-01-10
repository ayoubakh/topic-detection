import streamlit as st

def sidebar():
    lda_desc= "Latent Dirichlet Allocation (LDA) is an example of topic model and is\
                used to classify text in a document to a particular topic."



    st.sidebar.header('Latent Dirichlet Allocation')
    st.sidebar.caption(lda_desc)