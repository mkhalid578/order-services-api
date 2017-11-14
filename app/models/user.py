from app.models.base import BaseModel, db

class UserInfo(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password

	def __repr__(self):
		return '<Name %r>' % self.name
