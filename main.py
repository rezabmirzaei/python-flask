from flask import Flask

app = Flask(__name__)

### TODO Add:
# Rest API endpoints
# Session management
# API key authentication


@app.route('/')
def home():
    return 'Sceleton code for a simple Python/Flask application'


if __name__ == '__main__':
    app.run(use_reloader=False, debug=False, host='0.0.0.0', port=5002)
