from flask import request, session


def user_provided_api_key():
    # Check first headers for api key
    api_key = request.headers.get('x-api-key')
    # If no api key provided in headers, check url request params
    api_key = request.args.get('key') if api_key is None else api_key
    return api_key


def verify_api_key(user_provided_api_key):
    # Check first for valid session
    api_key = session['api_key'] if 'api_key' in session.keys() else None
    if (api_key is None):
        # TODO Get/check key validity from some source (e.g. DB with valid keys)
        api_key = 'test-key'
        session['api_key'] = api_key
    return user_provided_api_key == api_key
