from flask_restx import Api

from .info_ns import ns as info_ns
from .search_ns import ns as search_ns

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-api-key'
    }
}

api = Api(
    version='1.0',
    title='Python/Flask API skeleton code',
    description='Python/Flask API skeleton code',
    authorizations=authorizations
)

api.add_namespace(info_ns)
api.add_namespace(search_ns)
