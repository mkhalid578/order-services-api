from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from app.resources.orders import orders_api
from app.resources.users import users_api

app.register_blueprint(orders_api)
app.register_blueprint(users_api)


