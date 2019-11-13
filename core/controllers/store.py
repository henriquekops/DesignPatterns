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
from core.models.store import StoreModel


class StoreController(Resource):

    __model = StoreModel()

    def get(self):
        products = self.__model.show()
        return make_response(render_template('store.html', products=products))
