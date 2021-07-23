from functools import wraps
from utils import get_api_key

from flask import abort, request, session


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        # TODO Check key validity from some source (e.g. DB with valid keys)
        key = 'test-key'
        api_key = get_api_key()
        if api_key is not None and api_key == key:
            session['api_key'] = api_key
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
