import ecommerce
from ecommerce import store, models, views, auth, create_app
import pytest, os, urllib

def test_app_created():
    assert create_app() != None

def test_database_created():
    assert os.path.exists('ecommerce/db.sqlite3')

def test_log_file_created():
    assert os.path.exists('server.log')

@pytest.mark.parametrize('module', [ecommerce.models, ecommerce.auth, ecommerce.store])
def test_log_debug_mode(module):
    assert module.logger.level == 10
    #assert module.logger.level != 10

@pytest.mark.parametrize('route',['/','/contact', '/collection', '/racing_boots' , '/register', '/login'])
def test_routes(route):
    url = 'http://127.0.0.1:5000'+route
    resp = urllib.request.urlopen(url)
    assert resp.status == 200


