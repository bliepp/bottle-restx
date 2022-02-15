# Bottle RESTX
A simple resource based REST API extension for the bottle framework. Loosely inspired by flask-restx.

## Installation
**Via `pip`**
```bash
$ pip install bottle-restx
```

## Quickstart
The syntax is class based. Create an `API` object, which is a subclass of `bottle.Bottle`. For every resource add a subclass of the `Resource` class and decorate it with the `API.route` decorator. The route is passed to the method fitting the HTTP method.
```python
from bottle_restx import API, Resource
api = API()

@api.route("/my/route/<id>")
class MyResource(Resource):
    def get(id):
    ...
    def post(id):
    ...
    def put(id):
    ...
    def delete(id):
    ...
```
The individual methods are not mandatory. You might actually discard unwanted methods. By default they produce an 405 (Method not allowed).