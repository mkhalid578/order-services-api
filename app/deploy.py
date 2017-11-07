import os
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from json import dumps
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",config.SQL_DATABASE_URI)
db = SQLAlchemy(app)
api = Api(app)

@app.route("/")
def startPage():
	return "<h1> Default Page </h1>"

@app.route("/web")
def index():
    return render_template("index.html")

