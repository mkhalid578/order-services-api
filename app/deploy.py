import os
from flask import Flask, request, render_template, url_for, redirect
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
	return render_template("index.html")

@app.route("/web/login", methods=['GET', 'POST'])
def login():
        error = None
        if request.method == "POST":
                if request.form['email'] == "test@gmail.com" and request.form['password'] == 'password':
                        return redirect(url_for('dashboard'))
                else:
                        error = "Invalid Username or Password"

        return render_template("index.html", error=error)

@app.route("/web/dashboard")
def dashboard():
	return render_template("dashboard.html")
