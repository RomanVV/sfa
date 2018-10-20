from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Car:')
    submit = SubmitField('Add Car')


class DelForm(FlaskForm):

    id = IntegerField('Id of Car to Remove:')
    submit = SubmitField('Remove Car')
