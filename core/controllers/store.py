
from flask_restful import Resource


class StoreController(Resource):

    @staticmethod
    def get():
        return "Store"
