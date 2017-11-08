
from deploy import app
from flask import request, render_template, url_for, redirect

@app.route("/")
def startPage():
	return render_template("index.html")

@app.route("/web/login", methods=['GET', 'POST'])
def login():
        error = None
        if request.method == "POST":
                if request.form['email'] == "test@gmail.com" and request.form['password'] == 'password':
                        return redirect(url_for('dashboard'))
                else:
                        error = "Invalid Username or Password"

        return render_template("index.html", error=error)

@app.route("/web/dashboard")
def dashboard():
	return render_template("dashboard.html")
