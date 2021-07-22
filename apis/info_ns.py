from functools import wraps

from flask import abort, request
from flask_restx import Namespace, Resource, fields

# TODO Tmp solution for datastore
INFO = [
    {'id': '0', 'content': 'Python/Flask skeleton code'},
    {'id': '1', 'content': 'Information 1'},
    {'id': '2', 'content': 'Information 2'},
]

ns = Namespace('info', description='Information retrieval endpoints')

info_element = ns.model('Information element', {
    'id': fields.String(required=True, description='Identifier of information to retrieve'),
    'content': fields.String(required=True, description='The information')
})


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        key = 'test-key'
        if (request.args.get('key') and request.args.get('key') == key) or (request.headers.get('x-api-key') and request.headers.get('x-api-key') == key):
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


@ns.route('/')
class Info(Resource):

    @require_appkey
    def get(self):
        '''Fetch default information'''
        # return {'Python': 'Flask'}
        return INFO[0]


@ns.route('/<int:id>')
@ns.param('id', 'Identifier of information to retrieve')
class InfoID(Resource):

    @ns.marshal_with(info_element)
    def get(self, id):
        '''Fetch information with given identifier'''
        for info in INFO:
            if info['id'] == id:
                return info
        ns.abort(404)
