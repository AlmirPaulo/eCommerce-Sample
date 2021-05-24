from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, logging

app = Flask(__name__)

db = SQLAlchemy()

#Factory
def create_app():
    from . import models, views, auth, store
    app.config['SECRET_KEY'] = 'some really really secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #Initiate database
    db.init_app(app)

    #create database
    def create_db(app):
        if not os.path.exists('db.sqlite3'):
            return  db.create_all(app=app) 

    create_db(app)

    #Blueprints register
    from .store import store

    app.register_blueprint(store, url_prefix='/')

    return app
