C++ API Reference
==================

Generated from the public headers in ``src/webbridge/`` via Doxygen/Breathe.
See :doc:`concepts` for the narrative explanation of these types.

Namespace ``webbridge``
------------------------

Covers both ``object.h`` and ``error.h`` — documented together since Breathe
emits a duplicate namespace declaration if they're pulled in as two separate
``doxygenfile`` directives.

.. doxygennamespace:: webbridge
   :content-only:

property<T>
-----------

.. doxygenclass:: webbridge::impl::property
   :members:

event<Args...>
--------------

.. doxygenclass:: webbridge::impl::event
   :members:
