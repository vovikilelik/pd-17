from flask_restx import Resource
from abc import ABCMeta, abstractmethod


class Endpoint(Resource):
    __metaclass__ = ABCMeta

    def get(self, **args):
        try:
            data = self.get_data(**args)

            if not data:
                return 'Not Found', 404

            return data, 200
        except Exception as e:
            return str(e), 500

    @abstractmethod
    def get_data(self, **args):
        """Получить данные"""
