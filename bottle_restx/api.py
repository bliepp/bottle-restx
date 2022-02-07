import bottle


class API(bottle.Bottle):    
    # is a decorator
    def resource(self, cls):
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