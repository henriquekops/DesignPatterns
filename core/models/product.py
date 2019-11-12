
# built-in dependencies
from random import randint
from abc import ABC, abstractmethod


class ProductModel(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def __str__(self):
        return ', '.join([f'{k}:{v}' for k, v in self.__dict__.items()])


class HealthProduct(ProductModel):

    def __init__(self):
        self.name = "Health Product"
        self.price = randint(1, 20)
        self.type = "Health"

    def factory_method(self):
        return HealthProduct()


class TechProduct(ProductModel):

    def __init__(self):
        self.name = "Tech Product"
        self.price = randint(1, 20)
        self.type = "Tech"

    def factory_method(self):
        return TechProduct()


class HomeProduct(ProductModel):

    def __init__(self):
        self.name = "Home Product"
        self.price = randint(1, 20)
        self.type = "Home"

    def factory_method(self):
        return HomeProduct()