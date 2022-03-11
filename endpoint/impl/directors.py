from endpoint.endpoint import Endpoint
from endpoint.scheme.dict_scheme import dict_scheme, dict_list_scheme
from entity.director_entity import DirectorEntity
from flask_app import current_api

directors_ns = current_api.namespace('directors')


@directors_ns.route('/')
class DirectorsEndpoint(Endpoint):

    def get_data(self):
        rows = DirectorEntity.query.all()
        return dict_list_scheme.dumps(rows, ensure_ascii=False)


@directors_ns.route('/<int:director_id>')
class DirectorEndpoint(Endpoint):

    def get_data(self, director_id):
        row = DirectorEntity.query.get(director_id)
        return dict_scheme.dumps(row, ensure_ascii=False)
