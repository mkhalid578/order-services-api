from deploy import db
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
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

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    email = db.Column(db.String(120))
    position = db.Column(db.String(80))

    def __init__(self, firstName, lastName, email, position):
	db.create_all()
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.position = position

    def __repr__(self):
        return '<Name %r>' % self.name

    

order = Order("muhammed","khalid","mkhalid@uml.edu","Engineer")
db.session.add(order)
db.session.commit()

