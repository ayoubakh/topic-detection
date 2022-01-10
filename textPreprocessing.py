from os import name
import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import wordnet
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {'J': wordnet.ADJ,
                'N': wordnet.NOUN,
                'V': wordnet.VERB,
                'R': wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def textPreprocessing():
    # Upload dataset
    st.subheader('Upload Dataset')
    dataset = st.file_uploader("", type = ['csv'])
    if dataset is not None:
        df = pd.read_csv(dataset)
        st.write(df)

        # Text Preprocessing
        st.subheader('Text Preprocessing')
        with st.spinner('Wait! text preporocessing in progress'):
            with st.expander('Expand for details'):
                # remove duplicate rows
                st.subheader('Remove duplicate rows and lowercase text')
                df = df.drop_duplicates()
                # lowercase text
                df['clean_tweet'] = df['Text'].str.lower()
                st.table(df[['Text', 'clean_tweet']].head(2))

                # remove hyperlinks (http)
                st.subheader('Remove hyperlinks')
                df['clean_tweet'] = df["clean_tweet"].apply(lambda x: re.sub(r"http\S+", " ", x))
                st.table(df[['Text', 'clean_tweet']].head(2))

                # remove hashtags (#)
                st.subheader('Remove hashtags (#)')
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x: re.sub(r"\#\S+", " ", x))
                st.table(df[['Text', 'clean_tweet']].head(2))

                # remove user tag (@user)
                st.subheader('Remove user tag (@user)')
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x: re.sub(r"\@\S+", " ", x))
                st.table(df[['Text', 'clean_tweet']].head(2))
                
                # remove tweet handler ($)
                st.subheader('Remove tickers ($)')
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x: re.sub(r"\$\S+", " ", x))
                st.table(df[['Text', 'clean_tweet']].head(2))

                # remove ponctuation, number, special characters, and emojis
                st.subheader('Remove ponctuation, numbers and special characters')
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x: re.sub(r"[^A-z\t]", " ", x))
                st.table(df[['Text', 'clean_tweet']].head(2))

                # tokenize text
                st.subheader('Tokenization')
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x: nltk.word_tokenize(x))
                st.table(df[['Text', 'clean_tweet']].head(2))

                # lemmatizing text
                st.subheader('Lemmatization')
                lemmatizer = WordNetLemmatizer()
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x: [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in x])
                st.table(df[['Text', 'clean_tweet']].head(2))

                # Remove stop words
                st.subheader('Remove stop words')
                stop_words = set(stopwords.words('english'))
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x: [w for w in x if not w in stop_words])
                st.table(df[['Text', 'clean_tweet']].head(2))
                
                # Remove short words
                st.subheader('Remove short words')
                df['clean_tweet'] = df['clean_tweet'].apply(lambda x:  [w for w in x if len(w) > 2])
                st.table(df[['Text', 'clean_tweet']].head(2))

                # Joining all together
                df['clean_tweet']  = df['clean_tweet'].apply(lambda x: " ".join(x)) 
                st.table(df[['Text', 'clean_tweet']].head(2))
                

                st.dataframe(df)

        # Word cloud 
        with st.expander('Word Cloud'):
            generate_word_cloud(df)

        # Download csv file
        csv = df.to_csv(index=False).encode('utf-8')
        filename = dataset.name.replace('.csv', '_clean.csv')        
        st.download_button("Download the clean data", csv,filename, "text/csv",key='download-csv')


def generate_word_cloud(df):
    st.header('Word Cloud')
    long_string = ','.join(list(df['clean_tweet'].values))
    # Create a WordCloud object
    wordcloud = WordCloud(height=450, width=750, background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
    # Generate a word cloud
    wordcloud.generate(long_string)
    # Visualize the word cloud

    # word_cloud_image = wordcloud.to_image()
    # st.image(word_cloud_image, caption='Word Cloud')
    col1, col2, col3 = st.columns((2, 1, 1))
    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.pyplot()

    with col2:
        st.write(' ')
    
        