# METADATA
__author__ = ['Carlo Laitano', 'Henrique Kops', 'Larissa Salerno']
__date__ = '2019-11-11'
__version__ = 0.1

# external dependencies
from flask_restful import Resource
from flask import (
    render_template,
    make_response
)

# project dependencies
from core.services.generic import GenericService
from core.models.store import StoreModel


class StoreController(Resource):
    """ Store controller class """

    __service = GenericService()
    __model = StoreModel()

    def __init__(self):
        print(len(self.__model.show()))
        if len(self.__model.show()) == 0:
            self.__service.generate_products(self.__model)

    def get(self):
        products = self.__model.show()
        return make_response(render_template('store.html', products=products))

    def delete(self, product_id):
        self.__model.rem(product_id)
        products = self.__model.show()
        return make_response(render_template('store.html', products=products))
