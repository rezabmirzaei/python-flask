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


@ns.route('/')
class Info(Resource):
    def get(self):
        '''Fetch default information'''
        # return {'Python': 'Flask'}
        return INFO[0]


@ns.route('/<int:id>')
@ns.param('id', 'Identifier of information to retrieve')
@ns.response(404, 'Information not found')
class InfoID(Resource):
    @ns.marshal_with(info_element)
    def get(self, id):
        '''Fetch information with given identifier'''
        for info in INFO:
            if info['id'] == id:
                return info
        ns.abort(404)
