from flask import Flask
import pickle
import pandas as pd
from gensim import similarities

app = Flask(__name__)
app.config.from_object("app.config")

# unpickle my model
documents = pickle.load(open('app/models/documents.pkl','rb'))
dictionary = pickle.load(open('app/models/dictionary.pkl','rb'))
lsi = pickle.load(open('app/models/lsi.pkl','rb'))
corpus = pickle.load(open('app/models/corpus.pkl','rb'))
beers = pd.read_pickle('app/models/beer_review_df.pkl')
indexx = pickle.load(open('app/models/index.pkl','rb'))
corpus_tfidf = pickle.load(open('app/models/tfidf.pkl','rb'))

def get_beer_keywords(text_input, similar_beers):
	input_beer_keywords = []
	for item in sorted(corpus_tfidf[beers[beers.name == text_input].index[0]], key = lambda x: -x[1])[:5]:
		input_beer_keywords.append(dictionary[item[0]])

	similar_beer_words = []
	for beer in list(similar_beers.index):
	    similar_beer_words.append([dictionary[item[0]] for
	    	item in sorted(corpus_tfidf[beer], key = lambda x: -x[1])[:5]
	    	])#if dictionary[item[0]] in input_beer_keywords])
	return (input_beer_keywords, similar_beer_words)

def get_beer_names():
	return list(beers.name)

def get_brewery_names():
	return list(beers.brewery_name)

def similar_beers_formatting(beers):
	return zip(list(beers.name),list(beers.url),list(beers.brewery_name),list(beers.brewery_website))

def get_recs_from_input(text_input):
    beer_name_inputted = True
    try:
    	doc= documents[beers[beers.name == text_input].index[0]]
    except IndexError:
		doc = text_input
		beer_name_inputted = False
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]

    sims = indexx[vec_lsi]
    similar_beers = []
    for beer in sorted(enumerate(sims), key = lambda x: -x[1])[0:beer_name_inputted+5]:
        print(beers.name[beer[0]] + ' : %.2f' % (beer[1]*100))
        similar_beers.append(beer[0])
    similar_beers = beers.iloc[similar_beers]
    return (similar_beers,beer_name_inputted)

from .views import *


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
