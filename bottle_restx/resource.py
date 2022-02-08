import bottle



class Resource():
    """
    This class is intended to be derived from and used with the
    :py:meth:`bottle_restx.API.resource` decorator. A resource in REST
    can be thought of as a route whose meaning depends on the request
    method. For example: to define what should happen when requesting
    with GET, override the :py:meth:`get` method.

    Endpoint arguments:

    A route :code:`/my/route/<value>` in :py:meth:bottle_restx.Api.resource
    will produce an argument :code:`value` to be passed to the endpoints.
    
    :param args:
        Same as for regular bottle endpoints
    :param kwargs:
        Same as for regular bottle endpoints
    """
    
    def get(self, *args, **kwargs):
        """
        The endpoint for the GET request.
        """
        bottle.abort(405)

    def post(self, *args, **kwargs):
        """
        The endpoint for the POST request.
        """
        bottle.abort(405)

    def put(self, *args, **kwargs):
        """
        The endpoint for the PUT request.
        """
        bottle.abort(405)

    def delete(self, *args, **kwargs):
        """
        The endpoint for the DELETE request.
        """
        bottle.abort(405)