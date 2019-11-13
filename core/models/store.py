# METADATA
__author__ = ['Carlo Laitano', 'Henrique Kops', 'Larissa Salerno']
__date__ = '2019-11-11'
__version__ = 0.1


class StoreModel:
    """ Store model class """

    class __StoreModelInstance:

        def __init__(self):
            self.__products = list()

        def add(self, product):
            """ Method to add products into sale list """
            self.__products.append(product)

        def rem(self, product_index):
            """ Method to remove products into sale list """
            self.__products.pop(product_index)

        def show(self):
            """ Method to show all products in store """
            return self.__products

    instance = None

    def __init__(self):
        if not StoreModel.instance:
            StoreModel.instance = StoreModel.__StoreModelInstance()

    def __getattr__(self, name):
        return getattr(self.instance, name)
