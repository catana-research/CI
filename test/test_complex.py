from unittest import TestCase
from core import pmath
import math


class TestComplex(TestCase):
    """Test the Complex math class.


    TODO: Entich test cases
    """

    def setUp(self):
        """Setup test data.

        Complex numbers:
            c1 = 1 + 2i
            c2 = 2 - i
            c_real = 1 + 0i (Real)
            c_imag = 0 + i (Imaginary)

        :return: None
        """
        self.c1 = pmath.Complex(1, 2)
        self.c2 = pmath.Complex(2, -1)
        self.c_real = pmath.Complex(1, 0)
        self.c_imag = pmath.Complex(0, 1)
        return None

    def test_getter(self):
        self.fail()

    def test_setter(self):
        self.fail()

    def test_conjugate(self):
        self.assertEqual(self.c1.conjugate(), pmath.Complex(1, -2))

    def test_magnitude(self):
        """Test computation of complex magnitude.

        """
        self.assertEqual(self.c1.magnitude2(), 5)
        self.assertEqual(self.c1.magnitude(), math.sqrt(5))
        self.assertEqual(self.c2.magnitude(), math.sqrt(self.c2.magnitude()))

    def test_sub(self):
        """Test Complex subtraction.

        """
        # Complex number subtraction
        self.assertEqual(self.c1 - self.c2, pmath.Complex(-1, 3))
        self.assertEqual(self.c2 - self.c1, pmath.Complex(1, -3))

        # Complex and real subtraction
        self.assertEqual(self.c2 - 1, pmath.Complex(1, -1))
        self.assertEqual(1 - self.c2, pmath.Complex(-1, 1))
