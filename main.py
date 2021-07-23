import os
from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from apis import api
from flask_session import Session
from utils.caching import cache

# ENV VARS
load_dotenv()

# FLASK APP
app = Flask(__name__)

# CORS
CORS(app, supports_credentials=True)

# SESSION MANAGEMENT
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=3)
app.config['SESSION_FILE_THRESHOLD'] = 5
sess = Session(app)

# CACHING
cache.init_app(app)

# API
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT'))
