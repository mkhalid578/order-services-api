from flask import jsonify
from flask_restful import Resource

import models

class UserList(Resource):
        def get(self):
                return jsonify({'users': [{'user_one': 'Chocolate Milk'}]})

class User(Resource):
        def get(self, id):
                return jsonify({'user': 'Chocolate'})
        def put(self, id):
                return jsonify({'user': 'Chocolate'})
        def delete(self, id):
                return jsonify({'user': 'Chocolate'})
