from flask import Flask
import pickle
from gensim import similarities

app = Flask(__name__)
app.config.from_object("app.config")

# unpickle my model
documents = pickle.load(open('app/models/documents.pkl','rb'))
dictionary = pickle.load(open('app/models/dictionary.pkl','rb'))
lsi = pickle.load(open('app/models/lsi.pkl','rb'))
corpus = pickle.load(open('app/models/corpus.pkl','rb'))
beer_names = pickle.load(open('app/models/beer_names.pkl','rb'))
indexx = pickle.load(open('app/models/index.pkl','rb'))

def get_recs_from_input(text_input):
    beer_name_inputted = 1
    try:
        doc= documents[beer_names.index(text_input)]
    except ValueError:
        doc = text_input
        beer_name_inputted = 0
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]

    sims = indexx[vec_lsi]
    similar_beers = []
    for beer in sorted(enumerate(sims), key = lambda x: -x[1])[beer_name_inputted:beer_name_inputted+5]:
        print(beer_names[beer[0]] + ' : %.2f' % (beer[1]*100))
        similar_beers.append((beer_names[beer[0]],beer[1]))
    return similar_beers

from .views import *


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
