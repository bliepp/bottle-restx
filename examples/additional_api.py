#!/usr/bin/env python
"""
This example shows how to use the bottle_rest package
as a addition to an existing app built with the bottle
framework. It is loosely inspired by the syntax of the
flask-restx package.
"""

from bottle import Bottle
from bottle_restx import API, Resource


app = Bottle()
api = API()
app.mount("/api", api)

@api.route("/additional")
class TestResource(Resource):
    def get(self):
        return {"msg": "This is a response to a GET request."}
    def post(self):
        return {"msg": "This is a response to a POST request."}
    def put(self):
        return {"msg": "This is a response to a PUT request."}
    def delete(self):
        return {"msg": "This is a response to a DELETE request."}

@app.route("/")
def index():
    return "This is the index page"


if __name__ == "__main__":
    app.run()
