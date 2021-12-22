""" 
Data preprocessing

"""

import re
# nlp
import nltk
from nltk.corpus import wordnet
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords


class DataPreProcessor:

    """
    A class used to clean the data

    ...

    Attributes
    ----------
    data : Dataframe
        the data that we want to clean
    
    Methods
    -------
    
    """

    def __init__(self, data):
        self.data = data
        self.stopwords = stopwords.words('english')
    
    def cleaning(self):
        # remove hyperlinks
        self.data["Text_cleaned"] = self.data["Text"].apply(lambda x: re.sub(r"http\S+", " ", x))
        # remove hashtags
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(lambda x: re.sub(r"\#\S+", " ", x))
        # remove user tag
        self.data["Text_cleaned"] =self.data["Text_cleaned"].apply(lambda x: re.sub(r"\@\S+", " ", x))
        # remove tweet handler
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(lambda x: re.sub(r"\$\S+", " ", x))
        # remove ponctuation
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(lambda x: re.sub(r"[^A-z\t]", " ", x))
        # lowercase text
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(lambda x: x.lower())

        # tokenize text
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(lambda x: nltk.word_tokenize(x))
        # remove stop words
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(lambda x: [w for w in x if not w in self.stopwords])
        # remove stop words
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(lambda x: [w for w in x if len(w) > 2])
        # lemmatizing text
        lemmatizer = WordNetLemmatizer()
        self.data["Text_cleaned"] = self.data["Text_cleaned"].apply(
            lambda x: [lemmatizer.lemmatize(w, self.wordnet_pos(w)) for w in x])
        return self.data
    
    def wordnet_pos(self, word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {'J': wordnet.ADJ,
                    'N': wordnet.NOUN,
                    'V': wordnet.VERB,
                    'R': wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)

    def start(self):
        self.cleaning()
        
        return self.data
        pass