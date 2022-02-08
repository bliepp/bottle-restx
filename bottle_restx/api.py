import bottle
import json



class API(bottle.Bottle):
    """
    A child of :py:class:`bottle.Bottle` with members to handle
    :py:class:`Resource` classes using the decorator
    :py:meth:`resource`.
    """

    def default_error_handler(self, res):
        """
        The default error handler is overriden to make the API respond
        in :code:`application/json` content type format.
        """
        bottle.response.content_type = "application/json"
        return json.dumps(dict(error=res.body, status_code=res.status_code))
    
    def resource(self, path, **kwargs):
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
            self.route(path, "GET", instance.get, **kwargs)
            self.route(path, "POST", instance.post, **kwargs)
            self.route(path, "PUT", instance.put, **kwargs)
            self.route(path, "DELETE", instance.delete, **kwargs)
            return cls
        
        return wrapper