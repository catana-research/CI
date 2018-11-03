import math


class Complex(object):

    """Class for the creation and manipulation of complex numbers.

    """

    def __init__(self, real=0., imaginary=0.):
        """Constructor for the creation of a new complex number.

        Parameters
        ----------
        real : float
            Real component of the complex number.
        imaginary : float
            Imaginary component of the complex number.
        """
        self._real = float(real)
        self._imaginary = float(imaginary)
        return None

    # ------------------------------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------------------------------

    @property
    def real(self):
        """Provides access to the real component of the Complex number, :math:`Re(z)`.
        """
        return self._real

    @property
    def imaginary(self):
        """Provides access to the imaginary component of the Complex number, :math:`Im(z)`.
        """
        return self._imaginary

    @real.setter
    def real(self, real):
        self._real = real
        return None

    @imaginary.setter
    def imaginary(self, imaginary):
        self._imaginary = imaginary
        return None

    # ------------------------------------------------------------------------------------------
    # Methods
    # ------------------------------------------------------------------------------------------
    def conjugate(self):
        """Return the complex conjugate of a complex number :math:`z = a + bi`: :math:`z^{*} = a - bi`.

        Returns
        -------
        pmath.Complex
            Complex conjugate of input complex number.
        """
        return Complex(self._real, -self._imaginary)

    def magnitude(self):
        """Compute the magnitude of the complex number: :math:`|z| = \sqrt{zz^{*}}`.

        Returns
        -------
        pmath.Complex
            The magnitude of the input complex number.
        """
        magnitude_squared = self.magnitude2()
        return Complex(math.sqrt(magnitude_squared.real), math.sqrt(magnitude_squared.imaginary))

    def magnitude2(self):
        """Compute the square of the magnitude of the complex number: :math:`|z|^{2} = zz^{*}`

        Returns
        -------
        pmath.Complex
            The square of the magnitude of the input complex number.
        """
        return self * self.conjugate()

    # ------------------------------------------------------------------------------------------
    # Operators
    # ------------------------------------------------------------------------------------------
    def __neg__(self):
        return Complex(-self.real, -self.imaginary)

    def __add__(self, other):
        if type(other) is Complex:
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        else:
            return Complex(self.real + other, self.imaginary)

    __radd__ = __add__

    def __eq__(self, other):
        if type(other) is Complex:
            return self.real == other.real and self.imaginary == other.imaginary
        else:
            return self.real == other and self.imaginary == 0

    def __sub__(self, other):
        if type(other) is Complex:
            return Complex(self.real - other.real, self.imaginary - other.imaginary)
        else:
            return Complex(self.real - other, self.imaginary)

    def __rsub__(self, other):
        return Complex(other - self.real, -self.imaginary)

    def __mul__(self, other):
        if type(other) is Complex:
            return Complex(self.real * other.real - self._imaginary * other.imaginary,
                           self.real * other.imaginary + other.real * self.imaginary)
        else:
            return Complex(self.real * other, self.imaginary * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) is Complex:
            product = self * other.conjugate()
            magnitude2 = other.magnitude2().real
            return Complex(product.real / magnitude2, product.imaginary / magnitude2)
        else:
            return Complex(self.real / other, self.imaginary / other)

    def __rtruediv__(self, other):
        return Complex(other, 0) / self

    # ------------------------------------------------------------------------------------------
    # I/O
    # ------------------------------------------------------------------------------------------
    def __repr__(self):
        return f"pmath.Complex({self.real}, {self.imaginary})"

    def __str__(self):
        return f"({self.real}, {self.imaginary})"
