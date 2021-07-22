from flask import request
from flask_restx import Namespace, Resource, reqparse

ns = Namespace('search', description='Search endpoints')

parser = reqparse.RequestParser()
parser.add_argument('q', type=str, required=True,
                    help='The value to search for')


@ns.route('/')
@ns.param('q')
class Search(Resource):

    @ns.expect(parser)
    def get(self):
        '''Fetch search result'''
        if request.args.get('q') is None:
            ns.abort(400)
        return [{'key': 'value'}, {'key': 'value'}]
