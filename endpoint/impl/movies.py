from flask import request

from endpoint.endpoint import Endpoint
from endpoint.misc.utils import omit, send
from endpoint.scheme.movie_scheme import movie_list_scheme, movie_scheme
from entity.movie_entity import MovieEntity
from flask_app import current_api, current_db

movies_ns = current_api.namespace('movies')


@movies_ns.route('/')
class MoviesEndpoint(Endpoint):

    def get_data(self):
        page = request.args.get('page', 1)
        per_page = request.args.get('count', 10)

        filter_value = omit(request.args, 'page', 'count')

        rows = None
        if filter_value:
            rows = MovieEntity.query.filter_by(**filter_value).paginate(page, per_page)
        else:
            rows = MovieEntity.query.paginate(page, per_page)

        return movie_list_scheme.dumps(rows.items, ensure_ascii=False) if rows else None

    @staticmethod
    def add_data():
        data = request.json

        try:
            movie = MovieEntity(**data)
            current_db.session.add(movie)
            current_db.session.commit()
        except Exception as e:
            return 'Bad Request', 400

        return movie_scheme.dumps(movie, ensure_ascii=False), 201

    def post(self):
        return send(self.add_data)


@movies_ns.route('/<int:movie_id>')
class MovieEndpoint(Endpoint):

    def get_data(self, movie_id):
        row = MovieEntity.query.get(movie_id)
        return movie_scheme.dumps(row, ensure_ascii=False)

    @staticmethod
    def change_data(movie_id):
        data = request.json

        try:
            movie = MovieEntity(**data, id=movie_id)
            current_db.session.add(movie)
            current_db.session.commit()
        except Exception as e:
            return 'Bad Request', 400

        return movie_scheme.dumps(movie, ensure_ascii=False), 204

    @staticmethod
    def delete_data(movie_id):
        movie = MovieEntity.query.get(movie_id)

        if not movie:
            return 'Not Found', 404

        current_db.session.delete(movie)
        current_db.session.commit()

        return 'Not Content', 204

    def put(self, movie_id):
        return send(self.change_data, movie_id=movie_id)

    def delete(self, movie_id):
        return send(self.delete_data, movie_id=movie_id)
