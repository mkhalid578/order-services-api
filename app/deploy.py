import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from json import dumps
import config
from resources.orders import orders_api

app = Flask(__name__)
app.register_blueprint(orders_api)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",config.SQL_DATABASE_URI)
db = SQLAlchemy(app)
api = Api(app)


app.run()
