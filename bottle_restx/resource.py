import bottle



class Resource():
    """
    This class is intended to be derived from and used with the
    :py:meth:`API.route` decorator. A resource in REST can be
    thought of as a route whose meaning depends on the request method.
    For example: to define what should happen when requesting with
    GET, override the :py:meth:`get` method.

    Endpoint arguments:

    A route :code:`/my/route/<value>` in :py:meth:`API.route`
    will produce an argument :code:`value` to be passed to the endpoints.
    
    :param args:
        Same as for regular bottle endpoints
    :param kwargs:
        Same as for regular bottle endpoints
    """
    
    pass
