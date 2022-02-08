.. currentmodule:: bottle_restx

API
===

Core
----
.. autoclass:: API
   :members:

Resource
--------

.. autoclass:: Resource
   :members:
   :inherited-members:

   .. method:: get(*args, **kwargs)

      The endpoint for a GET request.

   .. method:: post(*args, **kwargs)

      The endpoint for a POST request.

   .. method:: put(*args, **kwargs)

      The endpoint for a PUT request.

   .. method:: patch(*args, **kwargs)

      The endpoint for a PATCH request.

   .. method:: delete(*args, **kwargs)

      The endpoint for a DELETE request.
