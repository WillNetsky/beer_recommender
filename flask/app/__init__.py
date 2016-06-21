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

def get_recs_from_input(text_input):
    beer_name_inputted = 1
    try:
    	doc= documents[beers[beers.name == text_input].index[0]]
    except IndexError:
		doc = text_input
		beer_name_inputted = 0
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]

    sims = indexx[vec_lsi]
    similar_beers = []
    for beer in sorted(enumerate(sims), key = lambda x: -x[1])[beer_name_inputted:beer_name_inputted+5]:
        print(beers.name[beer[0]] + ' : %.2f' % (beer[1]*100))
        similar_beers.append((beers.name[beer[0]],beer[1]))
    return similar_beers

from .views import *


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
