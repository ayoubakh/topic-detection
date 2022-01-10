import streamlit as st

def get_lda_params():
    col1, col2, col3 =  st.columns(3)
    with col1:
        num_topics = st.number_input('Number of topics', min_value=1, max_value=100, value=10, key="num-topic", 
                                    help="The number of requested latent topics to be extracted from the training corpus")

        alpha = st.selectbox('Alpha',('symmetric', 'asymmetric', 'auto'), key="alpha",
                            help="A-priori belief on document-topic distribution")
                        
    with col2:
        chunksize = st.number_input('chunksize', min_value=100, max_value=1000, value=100, key="chunk",
                                        help="Number of documents to be used in each training chunk")

        beta = st.selectbox('Beta',('symmetric', 'auto'), key="beta",
                                help="A-priori belief on topic-word distribution")
                        
    with col3:
        passes = st.number_input('Passes', min_value=1, max_value=1000, value=1, key="passes",
                                    help="Number of passes through the corpus during training.")

        iterations = st.number_input('Iterations', min_value=1, max_value=1000, value=50, key="iteration",
                                        help="Maximum number of iterations through the corpus when inferring the topic distribution of a corpus")


    lda_parametres = {'num_topics': num_topics,
                          'chunksize': chunksize,
                          'alpha': alpha,
                          'beta': beta,
                          'passes': passes,
                          'iterations': iterations
                          }

    return lda_parametres



def get_lda_results(topics):
    with st.expander('The Keywords in the topics'):
            topic_summaries = {}
            for topic in topics:
                topic_index = topic[0]
                topic_word_weights = topic[1]
                topic_summaries[topic_index] = ' + '.join(
                                                f'{weight:.3f} * {word}' for word, weight in topic_word_weights[:10])
            for topic_index, topic_summary in topic_summaries.items():
                st.markdown(f'**Topic {topic_index}**: _{topic_summary}_')