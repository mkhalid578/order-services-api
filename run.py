import config

from app import app, db

if __name__ == '__main__':
	app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
