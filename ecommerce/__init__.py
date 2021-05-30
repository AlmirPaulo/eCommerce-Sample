#https://flask-mail.readthedocs.io/en/latest/
#https://www.youtube.com/watch?v=48Eb8JuFuUI
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os, logging


#Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

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
    from .auth import auth
    app.register_blueprint(store, url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    #Set Up Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #?
    login_manager.init_app(app)
    
    from .models import User
    #Important!
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

