from flask import jsonify, Blueprint
from flask_restful import Resource, Api

class OrderList(Resource):
	def get(self):
		return jsonify({'orders': [{'order_one': 'Chocolate Milk'}]})
	
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
	'/api/v1/orders/<int:id>',
	endpoint='order'
)
