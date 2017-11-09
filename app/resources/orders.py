import json
from flask import jsonify, Blueprint, Response, abort
from flask_restful import (Resource, Api, reqparse,
			   inputs, fields, marshal,
			   marshal_with, url_for)

from app.models.orderInfo import OrderInfo

order_fields = {
	'id':fields.Integer,
	'email':fields.String,
	'itemName':fields.String,
	'quantity':fields.Integer,
	'cost':fields.Float,
	'description':fields.String
}

def get_order_or_404(order_id):
	try:
		order = OrderInfo.query.filter_by(id=order_id).first()
	except Exception as e:
		abort(404)
	else:
		return order


class OrderList(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('id',type=str)
		self.parser.add_argument('email', type=str, help="Email was not provided")
		self.parser.add_argument('itemName', type=str,required=True)
		self.parser.add_argument('quantity',type=int,required=True,help="missing quantity")
		self.parser.add_argument('cost',type=float,required=True)
		self.parser.add_argument('description',type=str,required=True)
		super().__init__()

	def get(self):
		orders = OrderInfo.query.all()
		payload = json.dumps (
			{
				'orders':[marshal(order, order_fields) for order in orders]
			}
		)
		return Response(payload, 200, mimetype='application/json')

	def post(self):
		args = self.parser.parse_args()
		print(args)
		try:
			order = OrderInfo(
					email=args['email'],
					itemName=args['itemName'],
					quantity=args['quantity'],
					cost=args['cost'],
					description=args['description']).create()

		except Exception as e:
			return Response(500)

		else:
			return

class Order(Resource):

	@marshal_with(order_fields)
	def get(self, id):
		return get_order_or_404(id)
	
	def put(self, id):
		return jsonify({'order': 'Chocolate'})
	def delete(self, id):
		return jsonify({'order': 'Chocolate'})

orders_api = Blueprint('resources.orders', __name__)
api = Api(orders_api)

api.add_resource(
	OrderList,
	'/api/v1/orders',
	endpoint='orders')

api.add_resource (
	Order,
	'/api/v1/order/<int:id>',
	endpoint='order')
