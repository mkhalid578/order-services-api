# NOTE: set login users, current user name on dashboard


from flask import Flask, render_template, request, session, flash, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json

import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


from app.resources.orders import orders_api
from app.resources.users import users_api
from app.resources.users import check_login_user
from app.resources.orders import save_place_order


app.register_blueprint(orders_api)
app.register_blueprint(users_api)


GLOBAL_LOGIN_USER_EMAILID = " "

#@login_manager.unauthorized_handler
#def unauthorized_callback():
#    return redirect('/index/')


@app.route('/index/', methods=['GET'])
def login_page():
    return render_template('index.html')



@app.route('/dashboard/', methods=['GET'])
#@login_required
def dashboard_page():
    return render_template('dashboard.html')

@app.route('/dashboard/user-email', methods=['GET'])
#@login_required
def dashboard_user_email():
    current_user_email = GLOBAL_LOGIN_USER_EMAILID 
    return current_user_email


@app.route('/dashboard/place-order', methods=['POST'])
#@login_required
def dashboard_place_order():
    new_order_data = request.args.get('key')
    db_new_order_data = json.loads(new_order_data)
    save_place_order(db_new_order_data)
    return "sucessfully added new order in database"



@app.route('/index/', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            user = check_login_user(request.form['email'])
            if request.form['email'] != user.email:
                error = 'Invalid User Email'
            elif request.form['password'] != user.password:
                error = 'Invalid Password'
            else:
                global GLOBAL_LOGIN_USER_EMAILID # needed to modify global copy
                GLOBAL_LOGIN_USER_EMAILID = (user.email)
                #login_user(user)
                return redirect(url_for('dashboard_page'))

        except AttributeError:
            error  = 'Invalid User Email ID or Password'

    return render_template('index.html', error=error)



@app.route('/logout/')
#@login_required
def UserLogout():
    #logout_user()
    return redirect(url_for('login_page'))
