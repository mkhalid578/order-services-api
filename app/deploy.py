import os
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from json import dumps
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",config.SQL_DATABASE_URI)
db = SQLAlchemy(app)
api = Api(app)

@app.route("/")
def index():
    return "<h1> Stuff </h1>"
