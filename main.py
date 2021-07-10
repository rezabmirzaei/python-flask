from datetime import timedelta

from flask import Flask, session
from flask_session import Session

app = Flask(__name__)

# TODO read from env
app.config['SECRET_KEY'] = '0f54d116-ae42-469e-8cd7-19496cb338dc'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
app.config['SESSION_FILE_THRESHOLD'] = 50
sess = Session(app)


@app.route('/set/<value>')
def set_session(value):
    session['value'] = value
    return f'The value you set is: { value }'


@app.route('/get')
def get_session():
    return f'The value in the session is: { session.get("value") }'


if __name__ == '__main__':
    app.run(use_reloader=False, debug=False, host='0.0.0.0', port=5002)
