#!/usr/bin/env python
"""
This example shows how to use the bottle_rest package
as a standalone API framwork. It is loosely inspired
by the syntax of the flask-restx package.
"""

from bottle_restx import API, Resource
import bottle


app = API()

@app.route("/<id:int>")
class TestResource(Resource):
    def get(self, id: int):
        return {"msg": f"This is a response to a GET request on resource {id}."}
    def post(self, id: int):
        return {"msg": f"This is a response to a POST request on resource {id}."}
    def put(self, id: int):
        return {"msg": f"This is a response to a PUT request on resource {id}."}
    def delete(self, id: int):
        return {"msg": f"This is a response to a DELETE request on resource {id}."}


if __name__ == "__main__":
    app.run()
