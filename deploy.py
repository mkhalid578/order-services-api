from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return '<h1> Deployed to Heroku!!!</h1>'
@app.route('/data')
def data():
    return "{'employee':'David Adams'}"

if __name__ == '__main__':
    app.run(debug=True)
