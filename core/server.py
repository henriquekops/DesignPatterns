
# external dependencies
from flask import Flask
from flask_restful import Api

# project dependencies
from core.controllers import (
    cart,
    store
)


def build():
    app = Flask(__name__)
    api = Api(app)

    __assign_resources(api)
    return app


def __assign_resources(api):
    route = 0
    controller = 1

    resources = (
        ('/', store.StoreController),
        ('/cart', cart.CartController)
    )

    for resource in resources:
        api.add_resource(resource[controller], resource[route])
