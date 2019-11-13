# METADATA
__author__ = ['Carlo Laitano', 'Henrique Kops', 'Larissa Salerno']
__date__ = '2019-11-12'
__version__ = 0.1

# built-in dependencies
from random import randint

# project dependencies
from core.models.product import ProductModel


class GenericService:

    __product = ProductModel()
    __types = ['health', 'tech', 'home']

    def generate_products(self, storage):
        for _ in range(5):
            p_type = self.__types[randint(0, 2)]
            storage.add(
                self.__product.factory_method(p_type)
            )
