from app.models.base import BaseModel, db

class OrderInfo(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(80))
	itemName  = db.Column(db.String(80))
	quantity = db.Column(db.Integer)
	cost = db.Column(db.Float)
	description = db.Column(db.String(250))

	def __init__(self, email, itemName, quantity, description, cost):
		self.email = email
		self.itemName = itemName
		self.quantity = quantity
		self.description = description
		self.cost = cost

		def __repr__(self):
			return '<Name %r>' % self.itemName
