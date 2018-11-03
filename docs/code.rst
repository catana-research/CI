The core API reference
======================



The Complex class
-----------------

Handles the creation and manipulation of complex numbers: :math:`Re(z) = a + bi`.

**Examples**

Creation of a new Complex numbers: :math:`z_{1} = 1 + i`, :math:`z_{2} = 2 + -i`:

>>> from core import pmath
>>> z1 = pmath.Complex(1, 1)
>>> z2 = pmath.Complex(2, -1)
>>> print(f'z1 = {z1}, z2 = {z2}')
z1 = (1, 1), z2 = (2.0, -1.0)

The complex number class handles a variety of complex mathematical operations, including omplex arithmetic:

>>> print(f'z1 - z2 = {z1 - z2}')
z1 - z2 = (-1.0, 2.0)
>>> print(f'z1 * z2 = {z1 * z2}')
z1 * z2 = (3.0, 1.0)

In addition to complex operations:

>>> print(f'|z1| = {z1.magnitude()}')
|z1| = (1.4142135623730951, 0.0)


.. autoclass:: pmath.Complex
   :members:

