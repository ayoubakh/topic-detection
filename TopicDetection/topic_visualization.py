# imports
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

def topic_visualization(model, corpus, id2word):
	vis = gensimvis.prepare(model, corpus, id2word)
	html_string = pyLDAvis.prepared_data_to_html(vis)
	return html_string