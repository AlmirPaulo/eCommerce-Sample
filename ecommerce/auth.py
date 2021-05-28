from flask import flash, request, redirect, Blueprint, url_for
from . import db, views, models, store
from .models import User 
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user 
import logging


#Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

#Set up Blueprint
auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        #variables
        username = request.form.get('username') 
        passwd = request.form.get('pass') 
        passwd_conf = request.form.get('conf-pass') 
        email = request.form.get('email') 
        abc = 'qwertyuiopasdfghjklzxcvbnm'
        num = '0123456789'
        
        def is_symbol(character):
            if character not in abc and character not in num:
                return True

        #validation
        if len(username) < 3:
            flash('Your username is too short', category='error')
        elif len(username) > 30:
            flash('Your username is too long',category='error')
        elif len(passwd) < 8:
            flash('Your password is too short',category='error')
        elif len(passwd) > 30:
            flash('Your password is too long', category='error')
        elif not any(i in passwd for i in num):
            flash('Your password should be alphanumeric, but it has no numbers', category='error')
        elif not any(i in passwd for i in abc):
            flash('Your password should be alphanumeric, but it has no lowercase letters',category='error')
        elif not any(i in passwd for i in abc.upper()):
            flash('Your passoword have not uppercase letters', category='error')
        elif not any(is_symbol(i) for i in passwd):
            flash('Your password should have at least one symbol', category='error')
        elif '@' not in email or '.' not in email:
            flash('This email, seems not legit...', category='error')
        #add new user to db
        else:
            new_user = User(username=username, password=generate_password_hash(passwd, method='sha256'), email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Congratulations! You are registered, now you can start to buy!', category='success')
    #como logar automaticamente?
    return views.register()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #variables
        username = request.form.get('username')
        passwd = request.form.get('pass')
                    #SqlAlchemy stuff
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, passwd):
                flash('Logged in succesfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('store.index'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Username does not exist', category='error')
    return views.login()

#criar pagina, procurar uma api que de conta da compra e o bootstrap acho que tem um apagina de cart

#Colocar botao para logout em algum lugar
@auth.route('/logout')
def logout():
    return redirect(url_for('store.index'))
