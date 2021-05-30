from flask import render_template

def index():
    return render_template('index.html')

def collection():
    return render_template('collection.html')

def contact():
    return render_template('contact.html')

def racing_boots():
    return render_template('racing_boots.html')

def shoes():
    return render_template('shoes.html')

def register():
    return render_template('register.html')

def login():
    return render_template('login.html')

def new_password():
    return render_template('new_password.html')
