import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

"""
in this file we are responsible for create the app, database setup, register blueprints
"""

#create app
app = Flask(__name__)
CORS(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True 
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_store.sqlite3'

app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"http://127.0.0.1:5000": {"origins": "*"}})

##########################################
############ DATABASE SETUP ##############
##########################################

#create a db and connect to the sqlitAlchemy
 
db = SQLAlchemy(app)

##########################################
######### REGISTER BLUEPRINTS ############
##########################################

from project.Categories.views import categories
from project.Fishes.views import fishes
from project.Meat_products.views import meat_products
from project.Milk_products.views import milk_products
from project.Pastries.views import pastries

app.register_blueprint(categories)
app.register_blueprint(fishes)
app.register_blueprint(meat_products)
app.register_blueprint(milk_products)
app.register_blueprint(pastries)


with app.app_context():
    db.create_all()