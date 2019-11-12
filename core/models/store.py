# METADATA
__author__ = ['Carlo Laitano', 'Henrique Kops', 'Larissa Salerno']
__date__ = '2019-11-11'
__version__ = 0.1


class StoreModel:
    """ Store model class """
    __instance = None

    class __StoreModelInstance:

        def __init__(self):
            self.__products = list()

        def add_product(self, product):

            """ Method to add procucts into sale list """

            try:

                self.__products.append(product)

            except Exception as e:
                raise Exception("Error to add product {}".format(str(e)))

        def remove_product(self, product_index):

            """ Method to remove procucts into sale list """

            try:

                self.__products.pop(product_index)

            except Exception as e:
                raise Exception('Error to remove product {}'.format(str(e)))

        def show_products(self):

            """ Method to show all products in store """

            return self.__products

    def __init__(self):
        if not self.__instance:
            StoreModel.__instance = StoreModel.__StoreModelInstance()
        print(self.__instance)

    def __getattr__(self, name):
        return getattr(self.__instance, name)


if __name__ == "__main__":
    import pdb; pdb.set_trace()
