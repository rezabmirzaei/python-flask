from flask_restx import Namespace, Resource, fields

# TODO Tmp solution for datastore
INFO = [
    {'id': '1', 'content': 'Information 1'},
    {'id': '2', 'content': 'Information 2'},
]

api = Namespace('get_info', description='Information retrieval endpoints (GET)')

info_element = api.model('Information element', {
    'id': fields.String(required=True, description='Identifier of information to retrieve'),
    'content': fields.String(required=True, description='The information')
})


@api.route('/<id>')
@api.param('id', 'Identifier of information to retrieve')
@api.response(404, 'Information not found')
class Info(Resource):
    @api.doc('get_info')
    @api.marshal_with(info_element)
    def get(self, id):
        '''Fetch information with given identifier'''
        for info in INFO:
            if info['id'] == id:
                return info
        api.abort(404)
