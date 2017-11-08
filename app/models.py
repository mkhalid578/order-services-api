from deploy import db
from flask_sqlalchemy import SQLAlchemy
import json

class  User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Name %r>' % self.name

class OrderInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    itemName  = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    cost = db.Column(db.Float)
    description = db.Column(db.String(250))

    class Meta:
        database = db

    def __init__(self, email, itemName, quantity, description, cost):
        db.create_all()
        self.email = email
        self.itemName = itemName
        self.quantity = quantity
        self.description = description
        self.cost = cost

    def __repr__(self):
        return '<Name %r>' % self.itemName
