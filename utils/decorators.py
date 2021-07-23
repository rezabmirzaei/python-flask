from functools import wraps

from flask import abort, request


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        # TODO Check key validity from some source (e.g. DB with valid keys)
        key = 'test-key'
        # Check headers first for api key
        api_key = request.headers.get('x-api-key')
        # If no api key provided in headers, check url request params
        api_key = request.args.get('key') if api_key is None else api_key
        if api_key is not None and api_key == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
