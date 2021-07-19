from flask_restx import Api

from .get_info_ns import api as get_info_ns

api = Api(
    version='1.0',
    title='Python/Flask API skeleton code',
    description='Python/Flask API skeleton code',
)

api.add_namespace(get_info_ns)
