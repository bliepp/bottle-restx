#!/usr/bin/env python
"""
This example shows how to use the bottle_rest package
as a standalone API framwork. It is loosely inspired
by the syntax of the flask-restx package.
"""

from bottle_restx import API, Resource


app = API()

@app.route("/simple")
class TestResource(Resource):
    def get(self):
        return {"msg": "This is a response to a GET request."}
    def post(self):
        return {"msg": "This is a response to a POST request."}
    def put(self):
        return {"msg": "This is a response to a PUT request."}
    def delete(self):
        return {"msg": "This is a response to a DELETE request."}
    def patch(self):
        return {"msg": "This is a response to a PATCH request."}


if __name__ == "__main__":
    app.run()
