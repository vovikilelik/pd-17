from sqlalchemy import Column, Integer, String, ForeignKey

from flask_app import current_db


class MovieEntity(current_db.Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    trailer = Column(String)
    year = Column(Integer)
    rating = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    director_id = Column(Integer, ForeignKey('director.id'))
