
# built-in dependencies
from random import randint
from abc import ABC


class __Product(ABC):

    def __str__(self):
        return ', '.join([f'{k}:{v}' for k, v in self.__dict__.items()])


class HealthProduct(__Product):

    def __init__(self):
        self.name = "Health Product"
        self.price = randint(1, 20)
        self.type = "Health"


class TechProduct(__Product):

    def __init__(self):
        self.name = "Tech Product"
        self.price = randint(1, 20)
        self.type = "Tech"


class HomeProduct(__Product):

    def __init__(self):
        self.name = "Home Product"
        self.price = randint(1, 20)
        self.type = "Home"


class ProductModel:

    __classes = dict(
        health=HealthProduct,
        tech=TechProduct,
        home=HomeProduct
    )

    @classmethod
    def factory_method(cls, method):
        def __error():
            raise NotImplementedError
        return cls.__classes.get(method, __error)()
