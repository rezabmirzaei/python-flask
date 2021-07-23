from functools import wraps
from utils import user_provided_api_key, verify_api_key

from flask import abort, request, session


def require_api_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        api_key = user_provided_api_key()
        if verify_api_key(api_key):
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
