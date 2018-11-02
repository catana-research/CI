

class Complex(object):
    """Complex number class.

    Handles the creation and manipulation of complex numbers.

    Example

    TODO: - Documentation, Testing

    """

    def __init__(self, real=0, imaginary=0):
        """Constructor for new complex number

        :param real float: Real component.
        :param imaginary float: Imaginary component.
        """
        self._real = real
        self._imaginary = imaginary
        return None

    # ------------------------------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------------------------------

    @property
    def real(self):
        """

        :return:
        """
        return self._real

    @property
    def imaginary(self):
        """

        :return:
        """
        return self._imaginary

    @real.setter
    def real(self, real):
        """

        :param real:
        :return:
        """
        self._real = real
        return None

    @imaginary.setter
    def imaginary(self, imaginary):
        """

        :param imaginary:
        :return:
        """
        self._imaginary = imaginary
        return None

    # ------------------------------------------------------------------------------------------
    # Methods
    # ------------------------------------------------------------------------------------------

    def conjugate(self):
        """

        :return core.math.Complex:
        """
        return Complex(self._real, -self._imaginary)

    def magnitude(self):
        """Compute the magnitude of the complex number

        :return core.math.Complex: The magnitude of the complex number.
        """
        magnitude_squared = self.magnitude2()
        return Complex(math.sqrt(magnitude_squared.real), math.sqrt(magnitude_squared.imaginary))

    def magnitude2(self):
        """Compute the square of the magnitude of the complex number.

        :return core.math.Complex: Square of the magnitude of the complex number.
        """
        return self * self.conjugate()

    # ------------------------------------------------------------------------------------------
    # Operators
    # ------------------------------------------------------------------------------------------
    def __neg__(self):
        """

        :return:
        """
        return Complex(-self.real, -self.imaginary)

    def __add__(self, other):
        """

        :param other:
        :return:
        """
        if type(other) is Complex:
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        else:
            return Complex(self.real + other, self.imaginary)

    __radd__ = __add__

    def __eq__(self, other):
        if type(self) is Complex and type(other) is Complex:
            return self.real == other.real and self.imaginary == other.imaginary
        elif type(self) is Complex:
            return self.real == other and self.imaginary == 0
        else:
            return other.real == self and other.imaginary == 0

    def __sub__(self, other):
        """Subtraction operator.

        :param other:
        :return core.math.Complex:
        """
        if type(other) is Complex:
            return Complex(self.real - other.real, self.imaginary - other.imaginary)
        else:
            return Complex(self.real - other, self.imaginary)

    def __rsub__(self, other):
        if type(other) is Complex:
            return Complex(other.real - self.real, other.imaginary - self.imaginary)
        else:
            return Complex(other - self.real, -self.imaginary)

    def __mul__(self, other):
        if type(other) is Complex:
            return Complex(self.real * other.real - self._imaginary * other.imaginary,
                           self.real * other.imaginary + other.real * self.imaginary)
        else:
            return Complex(self.real * other,
                           self.imaginary * other)
    __rmul__ = __mul__

    def __div__(self, other):
        raise NotImplementedError("Not implemented.")

    # ------------------------------------------------------------------------------------------
    # I/O
    # ------------------------------------------------------------------------------------------
    def __repr__(self):
        return f"Complex({self.real}, {self.imaginary})"

    def __str__(self):
        return f"({self.real}, {self.imaginary})"
