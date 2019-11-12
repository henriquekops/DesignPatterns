
# external dependencies
from flask_restful import Resource
from flask import (
    render_template,
    make_response
)


class StoreController(Resource):

    @staticmethod
    def get():
        return make_response(render_template('store.html', products=[]))
