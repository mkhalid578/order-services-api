import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

HOST = "0.0.0.0"

PORT = 5000

DEBUG = False

SECRET_KEY = "4245fdkfj3424-42k4-4243-434$%#"

DATABASE_CONFIG = {
    "DB_NAME": "d9vfqpvte2ppn3",
    "USERNAME": "iyrqdnemwmiawj",
    "PASSWORD": "c024be396990a710b1b20f31e77b527ef25df851f3e9afa4033c639188e399c7",
    "LOCATION": "ec2-54-163-229-169.compute-1.amazonaws.com",
    "PORT": "5432"
}

SQLALCHEMY_DATABASE_URI = \
                   "postgres://{USERNAME}:{PASSWORD}@{LOCATION}:{PORT}/{DB_NAME}".format(**DATABASE_CONFIG)

SQLALCHEMY_TRACK_MODIFICATIONS = True
