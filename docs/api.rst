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

   .. py:method:: get(*args, **kwargs)

      The endpoint for a GET request.

   .. py:method:: post(*args, **kwargs)

      The endpoint for a POST request.

   .. py:method:: put(*args, **kwargs)

      The endpoint for a PUT request.

   .. py:method:: patch(*args, **kwargs)

      The endpoint for a PATCH request.

   .. py:method:: delete(*args, **kwargs)

      The endpoint for a DELETE request.
