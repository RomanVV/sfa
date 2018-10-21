import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SECRET_KEY'] = 'bigsecret'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLACLHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

from myproject.cars.views import cars_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(cars_blueprint, url_prefix='/cars')
app.register_blueprint(owners_blueprint, url_prefix='/owners')
