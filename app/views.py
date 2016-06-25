
from flask import render_template
from flask import jsonify
from flask import request
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required

import pandas as pd
import json

from . import app, get_recs_from_input, get_beer_names, get_brewery_names, get_beer_keywords, similar_beers_formatting


beer_names = get_beer_names()
brewery_names = get_brewery_names()
beer_and_brewery = []
for beer, brewery in zip(beer_names,brewery_names):
    beer_and_brewery.append(dict(beer = beer, brewery = brewery))

class PredictForm(Form):
    """Fields for Predict"""
    myChoices = ["one", "two", "three"]
    beer_input = fields.StringField('Beer Name:', validators=[Required()])

    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():

    """Index page"""
    form = PredictForm()

    similar_beers = None
    beer_keywords = (None, None)
    beer_inputted = False

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        print(submitted_data)

        # Retrieve values from form
        beer_input = submitted_data['beer_input']

        # Get similar beer recommendations
        similar_beers = get_recs_from_input(beer_input)
        beer_inputted = similar_beers[1]
        
        beer_keywords = get_beer_keywords(beer_input,similar_beers[0])
        similar_beers = similar_beers_formatting(similar_beers[0])
        input_keywords = beer_keywords[0]
        similar_keywords = beer_keywords[1]


    return render_template('index.html', form=form, beer_inputted = beer_inputted, similar_beers=similar_beers, input_keywords = beer_keywords[0], similar_keywords = beer_keywords[1])

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('term')
    app.logger.debug(search)

    return jsonify(beer=beer_names, brewery = brewery_names)
