import bottle
import json



class API(bottle.Bottle):
    """
    A child of :py:class:`bottle.Bottle` with members to handle
    :py:class:`Resource` classes using the decorator
    :py:meth:`resource`.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__bottle_route("/", "GET", lambda: "")#bottle.template()) # route root to swagger ui

    def __bottle_route(self, *args, **kwargs):
        """
        Get bottle's route method to make room for the resources class
        decorator to be named route as well.
        """
        super().route(*args, **kwargs)

    def default_error_handler(self, res):
        """
        The default error handler is overriden to make the API respond
        in :code:`application/json` content type format.
        """
        bottle.response.content_type = "application/json"
        return json.dumps(dict(error=res.body, status_code=res.status_code))

    def mount(self, prefix, app, **kwargs):
        """
        Mount an application (:class:`API` or :class:`bottle.Bottle`)
        to a specific URL prefix. Example::

            api.mount('/other/', other_api)

        :param prefix: path prefix or `mount-point`. If it ends in a slash,
            that slash is mandatory.
        :param app: an instance of :class:`API` or :class:`bottle.Bottle`.
        """
        self.undoc()
        return super().mount(prefix, app, **kwargs)

    def route(self, path, **kwargs):
        """
        A decorator for a :py:class:`Resource` class
        to make it available at a specific route.
        """
        # ignore path and method keywords as they are set in the wrapper 
        kwargs.pop("path", None)
        kwargs.pop("method", None)

        # wrapper needed to pass arguments to decorator
        def wrapper(cls):
            instance = cls() # acts similar to a singleton
            for method in "get", "post", "put", "delete", "patch":
                if method_func := getattr(instance, method, None):
                    self.__bottle_route(path, method.upper(), method_func, **kwargs)
            return cls
        
        return wrapper

    def undoc(self):
        """
        Remove SwaggerUI documentation site for this API.
        """
        if "/" in self.router.builder.keys():
            del self.router.builder["/"]
        if "/" in self.router.static["GET"].keys():
            del self.router.static["GET"]["/"]
        del self.routes[0]
        pass