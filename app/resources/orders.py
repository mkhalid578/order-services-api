import json
from flask import jsonify, Blueprint, Response
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

def order_or_404(order_id):
	course = OrderInfo.filter_by(id=order_id).first()
	

class OrderList(Resource):
	def get(self):
		orders = OrderInfo.query.all()
		payload = json.dumps (
			{
				'orders':[marshal(order, order_fields) for order in orders]	
			}
		)
		return Response(payload, 200, mimetype='application/json')

class Order(Resource):
	def get(self, id):
		return jsonify({'order': 'Chocolate'})
	def put(self, id):
                return jsonify({'order': 'Chocolate'})
	def delete(self, id):
                return jsonify({'order': 'Chocolate'})

orders_api = Blueprint('resources.orders', __name__)
api = Api(orders_api)

api.add_resource(
	OrderList,
	'/api/v1/orders',
	endpoint='orders'
)

api.add_resource (
	Order,
	'/api/v1/order/<int:id>',
	endpoint='order'
)
