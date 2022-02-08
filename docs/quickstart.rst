Quickstart
==========

RESTful basics
--------------

:py:mod:`bottle-restx` is, as the name suggests, loosely inspired by
the syntax of :py:mod:`flask-restx`. RESTful APIs are based on
resources. This means that every resource is tied to a specific route
and depending on the HTTP method different tasks can be performed on
them.

Let's say your API provides a resource :code:`products` allowing the
users of your API to interact with your products stored in your
database. Performing a GET request on :code:`/products` might give you
a list of all products while performing a POST request might actually
add a new product.

To stay with that example: If you would like interact with a specific
product a resource :code:`/products/<id>` might be a good choice.
Again, performing a GET request gives you the product details of
the product with the given id while a DELETE request might actually
delete the product from the database.

Using bottle-restx
------------------

This package uses a class based approach as every resource is a
dedicated class inheriting from :py:class:`bottle_restx.Resource`.
The individual endpoints are implemented via member functions named
like the method they are supposed to map to. If a resource needs a GET
endpoint the class gets a :code:`get` method serving this purpose.
Using the :py:meth:`bottle_restx.API.resource` decorator serves this
purpose.

.. code-block::

    from bottle_restx import API, Resource
    api = API()
    
    @api.resource("/my/route/<id>")
    class MyResource(Resource):
        def get(id):
        ...
        def post(id):
        ...
        def put(id):
        ...
        def delete(id):
        ...

The individual methods are not mandatory. You might actually discard
unwanted methods. By default they produce an 405 (Method not allowed).
