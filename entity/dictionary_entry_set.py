from sqlalchemy import Column, String, Integer


class DictionaryEntitySet:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
