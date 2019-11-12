
# external dependencies
from flask_restful import Resource


class CartController(Resource):

    @staticmethod
    def get():
        return "Cart"
