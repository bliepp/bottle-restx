#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'bliepp'
__version__ = '1.0.1'
__license__ = 'MIT'


import bottle
import json






###############################################################################
# Resource Object ##############################################################
###############################################################################


class Resource():
    """
    This class is intended to be derived from and used with the
    :meth:`API.route` decorator. A resource in REST can be
    thought of as a route whose meaning depends on the request method.
    For example: to define what should happen when requesting with
    GET, set the :meth:`get` method.

    .. note::

       A route :code:`/my/route/<value>` in :meth:`API.route` will
       produce an argument :code:`value` to be passed to the endpoints
       via their :code:`*args` parameter. The parameters
       :code:`**kwargs` are directly passed from :meth:`API.route`.
    """
    pass # right now empty as it is solely used for type checking






###############################################################################
# API Object ###################################################################
###############################################################################


class API(bottle.Bottle):
    """
    A child of :class:`bottle.Bottle` with members to handle
    :class:`Resource` classes using the decorator :meth:`route`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.function_route("/", "GET", lambda: "") # route root to swagger ui

    def function_route(self, *args, **kwargs):
        """
        Get bottle's classic route method to make room for the resources class
        decorator to be named route as well. This is a decorator for functions.
        """
        super().route(*args, **kwargs)

    def default_error_handler(self, res):
        """
        The default error handler is overriden to make the API respond
        in :code:`application/json` content type format.
        """
        bottle.response.content_type = "application/json"
        return json.dumps(dict(error=res.body, status_code=res.status_code))

    def mount(self, prefix, app: "API", **kwargs):
        """
        Mount an application :class:`API` to a specific URL prefix.
        Example::

            parent_api.mount('/other/', child_api)

        Mounting an :class:`API` to another actually calls
        :meth:`undoc` on the mounted child object to make sure
        only the parent API uses SwaggerUI. A mounted :class:`API`
        basically acts like a namespace in flask-restx.

        :param prefix:
            path prefix or `mount-point`. If it ends in a slash, that
            slash is mandatory.
        :param app:
            an instance of :class:`API` or :class:`bottle.Bottle`.
        """
        if not isinstance(app, API):
            raise TypeError("Only bbjects of type bottle_restx.API are mountable.")
        app.undoc()
        return super().mount(prefix, app, **kwargs)

    def route(self, path, **kwargs):
        """
        A decorator for a :class:`Resource` class
        to make it available at a specific route.
        """
        # ignore method keyword as it is set implicitly in the wrapper
        kwargs.pop("method", None)

        # wrapper needed to pass arguments to decorator
        def wrapper(cls):
            instance = cls() # acts similar to a singleton
            for method in "get", "post", "put", "delete", "patch":
                if method_func := getattr(instance, method, None):
                    self.function_route(path, method.upper(), method_func, **kwargs)
            return cls
        
        return wrapper

    def undoc(self):
        """
        Remove SwaggerUI documentation site for the API this is called on.
        """
        if "/" in self.router.builder.keys():
            del self.router.builder["/"]
        if "/" in self.router.static["GET"].keys():
            del self.router.static["GET"]["/"]
        del self.routes[0]
        pass