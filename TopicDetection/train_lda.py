# gensim packages
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import numpy as np


def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))


def prepare_training_data(tweets):
    data = tweets.clean_tweet.values.tolist()
    data_words = list(sent_to_words(data))
    # Create Dictionary
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    return id2word, corpus



def train_lda(tweets, parametres):
    id2word, corpus = prepare_training_data(tweets)
    
    num_topics, chunksize, alpha, beta, passes, iterations = parametres['num_topics'], parametres['chunksize'], parametres['alpha'], \
                                                             parametres['beta'], parametres['passes'], parametres['iterations']

    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,  
                                                id2word=id2word,
                                                num_topics=num_topics,
                                                chunksize=chunksize,
                                                alpha=alpha,
                                                eta=beta,
                                                passes=passes,
                                                iterations=iterations) 

    return id2word, corpus, lda_model



def calculate_perplexity(model, corpus):
    return np.exp2(-model.log_perplexity(corpus))


def calculate_coherence(model, data_words, id2word, coherence):
    return CoherenceModel(model=model, texts=data_words, dictionary=id2word, coherence=coherence).get_coherence()

    