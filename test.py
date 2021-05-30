import ecommerce
from ecommerce import store, models, views, auth, create_app
import pytest, os, urllib, time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

#Webdriver Set Up
driver_options = Options()
driver_options.headless = True
driver = Firefox(options=driver_options)


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


login_test_parameters = [
    ('fulano','123'),
]



#Set Up
driver.get('http://localhost:5000/login')
time.sleep(2)

@pytest.mark.parametrize('user, passwd', login_test_parameters)
def test_login_validation(user, passwd):
    #variables
    input_user = driver.find_element_by_name('login')
    input_passwd = driver.find_element_by_name('pass')
    btn = driver.find_element_by_class_name('.btn-primary')
    #Test Process
    input_user.send_keys(user)
    input_passwd.send_keys(passwd)
    btn.click()
    #check
    time.sleep(1)
    assert driver.find_element_by_css_selector('.text-danger')

driver.quit()

#Set UP
#driver.get('http://127.0.0.1:5000/register')
#time.sleep(2)
#Tear Down
#driver.quit()
