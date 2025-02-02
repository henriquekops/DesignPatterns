# METADATA
__author__ = ['Carlo Laitano', 'Henrique Kops', 'Larissa Salerno']
__date__ = '2019-11-11'
__version__ = 0.1

# external dependencies
from flask_restful import Resource
from flask import (
    render_template,
    make_response,
    request
)

# project dependencies
from core.models.cart import CartModel


class CartController(Resource):
    """ Cart controller class """

    __model = CartModel()

    def get(self):
        products = self.__model.show()
        return make_response(render_template('cart.html', products=products))

    def post(self):
        product = request.form['product']
        self.__model.add(product)
        products = self.__model.show()
        return make_response(render_template('cart.html', products=products))
