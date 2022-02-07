class Resource():
    def __init__(self, api):
        self.api = api

    def get(self, *args, **kwargs):
        self.api.abort(405)

    def post(self, *args, **kwargs):
        self.api.abort(405)

    def put(self, *args, **kwargs):
        self.api.abort(405)

    def delete(self, *args, **kwargs):
        self.api.abort(405)