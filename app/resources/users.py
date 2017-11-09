from flask import jsonify, Blueprint
from flask_restful import Resource, Api

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

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)

api.add_resource (
	UserList,
	'/api/v1/users',
	endpoint='users'
)

api.add_resource (
	User,
	'/api/v1/user/<int:id>',
	endpoint='user'
)
