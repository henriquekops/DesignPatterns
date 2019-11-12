# METADATA
__author__ = ['Carlo Laitano', 'Henrique Kops', 'Larissa Salerno']
__date__ = '2019-11-11'
__version__ = 0.1


class CartModel:

    class __CartModelInstance:

        def __init__(self):
            self.__storage = list()

        def add(self, product):
            return self.__storage.append(product)

        def rem(self, product_id):
            return self.__storage.pop(product_id)

        def show(self):
            return self.__storage

    instance = None

    def __init__(self):
        if not CartModel.instance:
            CartModel.instance = CartModel.__CartModelInstance()

    def __getattr__(self, name):
        return getattr(self.instance, name)
