API
===

.. currentmodule:: bottle_restx

Core
----
.. autoclass:: API
   :members:

Resource
--------

.. autoclass:: Resource
   :members:
   :inherited-members:

   .. py:function:: get(*args, **kwargs)

      The endpoint for a GET request.

   .. py:function:: post(*args, **kwargs)

      The endpoint for a POST request.

   .. py:function:: put(*args, **kwargs)

      The endpoint for a PUT request.

   .. py:function:: patch(*args, **kwargs)

      The endpoint for a PATCH request.

   .. py:function:: delete(*args, **kwargs)

      The endpoint for a DELETE request.
