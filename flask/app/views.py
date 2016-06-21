
from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required
from autocomplete.forms import AutocompleteField
from autocomplete.views import autocomplete_view

import pandas as pd

from . import app, get_recs_from_input




class PredictForm(Form):
    """Fields for Predict"""
    myChoices = ["one", "two", "three"]
    beer_input = fields.StringField('Beer Name:', validators=[Required()])

    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():

    """Index page"""
    form = PredictForm()
    prediction = (None, None)

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        print(submitted_data)

        # Retrieve values from form
        beer_input = submitted_data['beer_input']

        #my_prediction = estimator.predict(flower_instance)
        # Return only the Predicted iris species
        prediction = get_recs_from_input(beer_input)

    return render_template('index.html', form=form, beer_inputted = prediction[1], similar_beers=prediction[0])
