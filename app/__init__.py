from __future__ import print_function

from flask import Flask
import pickle
import pandas as pd
from gensim import similarities

import sqlalchemy

import config

app = Flask(__name__)
app.config.from_object("app.config")

engine = sqlalchemy.create_engine(config.SQL_URL)
beers = pd.read_pickle('app/models/beer_review_df.pkl')
beer_names = list(beers.name)
brewery_names = list(beers.brewery_name)
search_strings = list(beers.search_string)
beers = None

def get_beer_names():
    return beer_names

def get_brewery_names():
    return brewery_names

def get_search_strings():
    return search_strings

def get_beer_keywords(text_input):
    connection = engine.connect()
    t = sqlalchemy.sql.expression.text('select * from beers where name = :name')
    sql_result = connection.execute(t,name = text_input)
    result = sql_result.first()
    connection.close()
    return ([result['kw1'],result['kw2'],result['kw3'],result['kw4'],result['kw5']],
            [result['sim_id_1'],result['sim_id_2'],result['sim_id_3'],result['sim_id_4'],result['sim_id_5']])

def get_similar_beer_info(similar_beers):
    connection = engine.connect()
    query = 'select * from beers where '
    
    query += 'index = ' + str(similar_beers[0])
    for beer in similar_beers[1:]:
        query += ' or index = ' + str(beer)
        
    sql_result = connection.execute(query)
    
    names = []
    urls = []
    breweries = []
    websites = []
    all_keywords = []
    for row in sql_result:
        names.append(row['name'])
        urls.append(row['url'])
        breweries.append(row['brewery_name'])
        websites.append(row['brewery_website'])
        keywords = [row['kw1'],row['kw2'],row['kw3'],row['kw4'],row['kw5']]
        all_keywords.append(keywords)
    connection.close()
    return zip(zip(names,urls,breweries,websites),all_keywords)

def get_beer_info(text_input):
    connection = engine.connect()
    t = sqlalchemy.sql.expression.text('select * from beers where name = :name')
    sql_result = connection.execute(t,name = text_input)
    result = sql_result.first()
    connection.close()
    return (result['name'],result['url'],result['brewery_name'],result['brewery_website'])

from .views import *


# Handle Bad Requests
@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found"""
    return render_template('404.html'), 404
