from flask_app import current_db
from entity.dictionary_entry_set import DictionaryEntitySet


class DirectorEntity(DictionaryEntitySet, current_db.Model):
    __tablename__ = 'director'
