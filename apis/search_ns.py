from flask import request
from flask_restx import Namespace, Resource, reqparse
from utils.caching import cache

ns = Namespace('search', description='Search endpoints')

parser = reqparse.RequestParser()
parser.add_argument('q', type=str, required=True,
                    help='The value to search for')


@ns.route('/')
@ns.param('q')
class Search(Resource):

    @ns.expect(parser)
    @ns.doc(responses={400: 'Missing parameter (\'q\')'})
    @cache.cached(timeout=3600, query_string=True)  # Cached for 1hr
    def get(self):
        '''Fetch search result'''
        if request.args.get('q') is None:
            ns.abort(400)
        return [{'key': 'value'}, {'key': 'value'}]
