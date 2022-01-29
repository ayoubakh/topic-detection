import streamlit as st

from TopicDetection.lda_params import get_lda_results
from TopicDetection.topic_visualization import topic_visualization
from TopicDetection.train_lda import train_lda_iterative
from streamlit import components

def get_iterative_lda_params():
	col1, col2, col3 = st.columns(3)
	with col1:
		min_num_topics = st.number_input('Minimum number of topics', min_value=3, max_value=100, value=3, key="min-num-topic",
			help="The minimum number of requested latent topics to be extracted from the training corpus")

		chunksize = st.number_input('chunksize', min_value=100, max_value=1000, value=100, key="chunk",
			help="Number of documents to be used in each training chunk")

		beta = st.selectbox('Beta', ('symmetric', 'auto'), key="beta",
			help="A-priori belief on topic-word distribution")

	with col2:
		max_num_topics = st.number_input('Max number of topics', min_value=4, max_value=100, value=10, key="max-num-topic",
			help="The maximum number of requested latent topics to be extracted from the training corpus")
		passes = st.number_input('Passes', min_value=1, max_value=1000, value=1, key="passes",
			help="Number of passes through the corpus during training.")
		iterations = st.number_input('Iterations', min_value=1, max_value=1000, value=50, key="iteration",
			help="Maximum number of iterations through the corpus when inferring the topic distribution of a corpus")

	with col3:
		step = st.number_input('topics skips', min_value=1, max_value=100, value=2, key="step",
			help="The number of latent topics to skip")
		alpha = st.selectbox('Alpha', ('symmetric', 'asymmetric', 'auto'), key="alpha",
			help="A-priori belief on document-topic distribution")


	lda_parametres = {'min_num_topics': min_num_topics,
			'max_num_topics': max_num_topics,
			'step': step,
			'chunksize': chunksize,
			'alpha': alpha,
			'beta': beta,
			'passes': passes,
			'iterations': iterations
		}

	return lda_parametres


def iterative_method(tweets):
	st.subheader('Iterative method')
	with st.form('iterative_lda'):
		parameters = get_iterative_lda_params()
		submitted = st.form_submit_button('Train')
		if submitted:
			id2word, corpus, models, coherence_s = train_lda_iterative(tweets, parameters)
			index_best_model = coherence_s.index(max(coherence_s))
			best_num_topics = index_best_model + parameters['min_num_topics']

			st.markdown(f"**best number of topics is {best_num_topics}**")

			# LDA Results
			topics = models[index_best_model].show_topics(formatted=False, num_words=50, num_topics=best_num_topics,
				log=False)
			get_lda_results(topics)

			# LDA Evaluation
			with st.expander('LDA Evaluation metric'):
				st.write('Coherence')
				st.write(coherence_s[index_best_model])

			# Pyldavis
			with st.spinner('Preparing visualization'):
				# st.subheader('Topics visualization')
				with st.expander('Topics visualization'):
					html = topic_visualization(models[index_best_model], corpus, id2word)
					components.v1.html(html, width=1300, height=800)
	pass
