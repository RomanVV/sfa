from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Owner:')
    car_id = IntegerField("Id of Car: ")
    submit = SubmitField('Add Owner')
