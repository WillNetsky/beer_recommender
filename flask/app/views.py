
from flask import render_template
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required
from autocomplete.forms import AutocompleteField
from autocomplete.views import autocomplete_view

import pickle
import os

from . import app, get_recs_from_input




class PredictForm(Form):
    """Fields for Predict"""
    myChoices = ["one", "two", "three"]
    beer_input = fields.StringField('Beer Name:', validators=[Required()])

    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():
    
    # # unpickle my model
    # documents = pickle.load(open('app/models/documents.pkl','rb'))
    # dictionary = pickle.load(open('app/models/dictionary.pkl','rb'))
    # lsi = pickle.load(open('app/models/lsi.pkl','rb'))
    # corpus = pickle.load(open('app/models/corpus.pkl','rb'))
    # beer_names = pickle.load(open('app/models/beer_names.pkl','rb'))
    # index = pickle.load(open('app/models/index.pkl','rb'))

    # def get_recs_from_input(text_input):
    #     beer_name_inputted = 1
    #     try:
    #         doc= documents[beer_names.index(text_input)]
    #     except ValueError:
    #         doc = text_input
    #         beer_name_inputted = 0
    #     vec_bow = dictionary.doc2bow(doc.lower().split())
    #     vec_lsi = lsi[vec_bow]

    #     sims = index[vec_lsi]
    #     similar_beers = []
    #     for beer in sorted(enumerate(sims), key = lambda x: -x[1])[beer_name_inputted:beer_name_inputted+5]:
    #         print(beer_names[beer[0]] + ' : %.2f' % (beer[1]*100))
    #         similar_beers.append((beer_names[beer[0]],beer[1]))
    #     return similar_beers

    """Index page"""
    form = PredictForm()
    prediction = None

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        print(submitted_data)

        # Retrieve values from form
        beer_input = submitted_data['beer_input']

        #my_prediction = estimator.predict(flower_instance)
        # Return only the Predicted iris species
        prediction = get_recs_from_input(beer_input)

    return render_template('index.html', form=form, prediction=prediction)
