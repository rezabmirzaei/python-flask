from flask_restx import Namespace, Resource

ns = Namespace('search', description='Search endpoints')


@ns.route('/')
@ns.param('q')
class Search(Resource):
    def get(self):
        '''Fetch search result'''
        return [{'key': 'value'}, {'key': 'value'}]
