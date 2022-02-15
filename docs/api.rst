.. module:: bottle_restx
   :platform: Unix, Windows
   :synopsis: Bottle framework extension
.. moduleauthor:: bliepp

API
===

The :class:`API` Class
----------------------
.. autoclass:: API
   :members:

The :class:`Resource` Class
---------------------------
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
