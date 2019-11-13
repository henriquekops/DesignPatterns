# METADATA
__author__ = ['Carlo Laitano', 'Henrique Kops', 'Larissa Salerno']
__date__ = '2019-11-11'
__version__ = 0.1


class CartModel:
    """ Cart model class """

    class __CartModelInstance:

        __status_cart = None

        def __init__(self):
            self.__storage = list()

        def add(self, product):
            """ Add product to the cart """
            self.__storage.append(product)
            self.verify_status_cart()

            return self.__storage

        def rem(self, product_id):
            """ Remove product from the cart """
            self.__storage.pop(product_id)
            self.verify_status_cart()

            return self.__storage

        def show(self):
            """ List all cart products """
            return self.__storage

        def verify_status_cart(self):
            print(self.__status_cart)
            print(self.__storage)
            if self.__status_cart != self.__storage:
                print("\n######## Cart modified ########\n######## Owner was notyfied ######## ")
                self.__status_cart = self.__storage.copy()

    instance = None

    def __init__(self):
        if not CartModel.instance:
            CartModel.instance = CartModel.__CartModelInstance()

    def __getattr__(self, name):
        return getattr(self.instance, name)
