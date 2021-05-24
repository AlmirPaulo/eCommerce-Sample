from . import db
import logging

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    credit_card = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return '<Shoes %r>' % self.title



