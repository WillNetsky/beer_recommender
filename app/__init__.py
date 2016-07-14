from flask import Flask
import pickle
import pandas as pd
from gensim import similarities

app = Flask(__name__)
app.config.from_object("app.config")

beers = pd.read_pickle('app/models/beer_review_df.pkl')
print 'beer_df loaded'

def get_beer_names():
    return list(beers.name)

def get_brewery_names():
    return list(beers.brewery_name)

def get_beer_keywords(text_input):
	beer_keywords = list(beers[beers.name == text_input].keywords)
	return (beer_keywords)

def get_similar_beer_keywords(similar_beers):
    keywords = list(similar_beers.keywords)
    return keywords

def get_beer_info(text_input):
    beer_info = beers[beers.name == text_input]
    return beer_info

def get_recs_from_input(text_input):
    beer_name_inputted = True

    similar_beer_ids = list(beers[beers.name == text_input].similar_beers)
    similar_beers = [beer[0] for beer in similar_beer_ids[0]]
    similar_beers = beers.iloc[similar_beers]
    return (similar_beers ,beer_name_inputted)

def similar_beers_formatting(beers):
    return zip(list(beers.name),list(beers.url),list(beers.brewery_name),list(beers.brewery_website))

from .views import *


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
