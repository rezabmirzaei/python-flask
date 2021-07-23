from datetime import timedelta

from flask import Flask, session

from apis import api
from flask_session import Session
from utils.caching import cache

# FLASK APP
app = Flask(__name__)

# SESSION MANAGEMENT
# TODO read from env
app.config['SECRET_KEY'] = '0f54d116-ae42-469e-8cd7-19496cb338dc'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
app.config['SESSION_FILE_THRESHOLD'] = 50
sess = Session(app)

# CACHING
cache.init_app(app)

# API
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
