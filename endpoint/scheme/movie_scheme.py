from marshmallow import Schema, fields

class MovieScheme(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()


movie_scheme = MovieScheme()
movie_list_scheme = MovieScheme(many=True)
