from flask import request, session


def get_api_key():
    # Check first for valid session
    api_key = session['api_key'] if 'api_key' in session.keys() else None
    if (api_key is None):
        # If not already a valid session, check headers for api key
        api_key = request.headers.get('x-api-key')
        # If no api key provided in headers, check url request params
        api_key = request.args.get('key') if api_key is None else api_key
    return api_key
