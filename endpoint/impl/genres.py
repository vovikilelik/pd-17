from endpoint.endpoint import Endpoint
from endpoint.scheme.dict_scheme import dict_scheme, dict_list_scheme
from entity.genre_entity import GenreEntity
from flask_app import current_api

genres_ns = current_api.namespace('genres')


@genres_ns.route('/')
class GenresEndpoint(Endpoint):

    def get_data(self):
        rows = GenreEntity.query.all()
        return dict_list_scheme.dumps(rows, ensure_ascii=False)


@genres_ns.route('/<int:genre_id>')
class GenreEndpoint(Endpoint):

    def get_data(self, genre_id):
        row = GenreEntity.query.get(genre_id)
        return dict_scheme.dumps(row, ensure_ascii=False)
