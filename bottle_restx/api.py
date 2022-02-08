import bottle


class API(bottle.Bottle):
    """
    A child of :py:class:`bottle.Bottle` with members to handle
    :py:class:`bottle_restx.Resource` classes using the decorator
    :py:meth:`resource`.
    """

    # is a decorator
    def resource(self, cls):
        """
        A decorator for a :py:class:`bottle_restx.Resource` class
        to make it available at a specific route.
        """
        __init__copy = cls.__init__

        def __init__(other, *args, **kwargs):
            # pass api object
            __init__copy(other, self)

        cls.__init__ = __init__

        instance = cls()
        self.route("/test", "GET", instance.get)
        self.route("/test", "POST", instance.post)
        self.route("/test", "PUT", instance.put)
        self.route("/test", "DELETE", instance.delete)

        # no need to return for this decorator since this class is never directly used