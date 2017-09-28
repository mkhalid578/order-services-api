from app.deploy import app, api
from app.models import User
from flask_restful import Api, Resource

@app.route('/')
def index():
    return '<h1> Welcome </h1>'

class UserData(Resource):
    def get(self, email):
        user = User.query.filter_by(email=str(email)).first()
        result = {'data' : user.name}
        return result

api.add_resource(UserData, '/data/<string:email>')



app.run(host="0.0.0.0", port="5000")
