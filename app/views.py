
from flask import render_template
from flask import jsonify
from flask import request
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required

import pandas as pd
import json

from . import app, get_recs_from_input, get_beer_info, get_similar_beer_keywords, get_beer_names, get_brewery_names, get_beer_keywords, similar_beers_formatting


beer_names = get_beer_names()
brewery_names = get_brewery_names()
beer_and_brewery = []
for beer, brewery in zip(beer_names,brewery_names):
    beer_and_brewery.append(dict(beer = beer, brewery = brewery))

class PredictForm(Form):
    """Fields for Predict"""
    myChoices = ["one", "two", "three"]
    beer_input = fields.StringField('Search for a Beer:', validators=[Required()])

    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():

    """Index page"""
    form = PredictForm()

    similar_beers = [None]*6
    beer_keywords = (None, [None]*6)
    beer_inputted = False
    input_beer_keywords = [None]*5
    input_beer = None
    similar_beer_keywords = None

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        print(submitted_data)

        # Retrieve values from form
        beer_input = submitted_data['beer_input']
        
        # Input beer info
        input_beer = get_beer_info(beer_input)
        input_beer = similar_beers_formatting(input_beer)
        input_beer_keywords = get_beer_keywords(beer_input)

        # Get similar beer recommendations
        recs = get_recs_from_input(beer_input)
        beer_inputted = recs[1]
        similar_beers = recs[0]
        similar_beer_keywords = get_similar_beer_keywords(similar_beers)
        similar_beers = similar_beers_formatting(similar_beers)
        similar_beers = zip(similar_beers,similar_beer_keywords)

    return render_template('index.html', form=form, beer_inputted = beer_inputted,
        similar_beers= similar_beers,
        similar_beer_keywords = similar_beer_keywords,
        input_beer = input_beer,
        input_beer_keywords = input_beer_keywords)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('term')
    #app.logger.debug(search)

    return jsonify(beer=beer_names, brewery = brewery_names)
