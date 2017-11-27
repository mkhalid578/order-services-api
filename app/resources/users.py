import json
from flask import jsonify, Blueprint, Response
from flask_restful import (Resource, Api, reqparse,
			   inputs, fields, marshal,
			   marshal_with, url_for)

from app.models.user import UserInfo




user_fields = {
	'id':fields.Integer,
	'name':fields.String,
	'email':fields.String,
	'password':fields.String,
}

def get_user_or_404(user_id):
    try:
        login_user = UserInfo.query.filter_by(id=user_id).first()
    except Exception as e:
        abort(404)
    else:
        return login_user

class UserList(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id',type=str)
        self.parser.add_argument('name', type=str, help="Email was not provided")
        self.parser.add_argument('email', type=str,required=True)
        self.parser.add_argument('password',type=str,required=True,help="missing quantity")
        super().__init__()

    def get(self):
        users = UserInfo.query.all()
        payload = json.dumps (
            {
                'users':marshal(users, user_fields) for user in users
            })
        return Response(payload, 200, mimetype='application/json')

    def post(self):
        args = self.parser.parse_args()
        print(args)
        try:
            user = UserInfo(
                name=args['name'],
                email=args['email'],
                password=args['password']).create()

        except Exception as e:
            return Response(500)

        else:
            return Response(json.dumps(marshal(user, user_fields)), 200)

class User(Resource):
        @marshal_with(user_fields)
        def get(self, id):
            return get_user_or_404(id)
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



def check_login_user(email_id):
    try:
        login_user = UserInfo.query.filter_by(email=email_id).first()
    except Exception as e:
        abort(404)
    else:
        return login_user

