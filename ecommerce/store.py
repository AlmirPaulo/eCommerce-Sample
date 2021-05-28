from . import views
from flask_login import login_required
from flask import Blueprint
import logging


#Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

store = Blueprint('store', __name__)


@store.route('/', methods=['GET', 'POST'])
def index():
    return views.index()

@store.route('collection')
def collection():
    return views.collection()

@store.route('contact', methods=['GET', 'POST'])
def contact():
    return views.contact()

@store.route('racing_boots')
def racing_boots():
    return views.racing_boots()

@store.route('shoes')
def shoes():
    return views.shoes()

@store.route('/cart')
@login_required
def cart():
    pass
#criar pagina, procurar uma api que de conta da compra e o bootstrap acho que tem um apagina de cart
