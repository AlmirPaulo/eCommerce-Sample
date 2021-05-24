from . import views
from flask import Blueprint


store = Blueprint('store', __name__)

@store.route('/')
def index():
    return views.index()

@store.route('collection')
def collection():
    return views.collection()

@store.route('contact')
def contact():
    return views.contact()

@store.route('racing_boots')
def racing_boots():
    return views.racing_boots()

