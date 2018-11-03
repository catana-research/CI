import unittest
from core import pmath
import math


class TestComplex(unittest.TestCase):
    """Test the Complex math class.


    TODO: Enrich test cases
    """

    def setUp(self):
        """Setup test data.

        Complex numbers:
            c1 = 1 + 2i
            c2 = 2 - 1i
            c_real = 1 + 0i (Real)
            c_imag = 0 + 1i (Imaginary)

        :return: None
        """
        self.c1 = pmath.Complex(1, 2)
        self.c2 = pmath.Complex(2, -1)
        self.c_real = pmath.Complex(1, 0)
        self.c_imag = pmath.Complex(0, 1)
        return None

    def test_getter(self):
        self.assertEqual(self.c1.real, 1)
        self.assertEqual(self.c1.imaginary, 2)

    def test_setter(self):
        self.c1.real = 2
        self.assertEqual(self.c1.real, 2)
        self.c1.imaginary = 3
        self.assertEqual(self.c1.imaginary, 3)

    def test_conjugate(self):
        self.assertEqual(self.c1.conjugate(), pmath.Complex(1, -2))
        self.assertEqual(self.c_real.conjugate(), self.c_real)
        self.assertEqual(self.c_imag.conjugate(), -self.c_imag)

    def test_magnitude(self):
        """Test computation of complex magnitude.

        """
        self.assertEqual(self.c1.magnitude2(), pmath.Complex(5, 0))
        self.assertEqual(self.c1.magnitude(), pmath.Complex(math.sqrt(5), 0))
        self.assertEqual(self.c2.magnitude(), pmath.Complex(math.sqrt(self.c2.magnitude2().real), 0))
        self.assertEqual(self.c_real.magnitude2(), pmath.Complex(1, 0))
        self.assertEqual(self.c_imag.magnitude2(), pmath.Complex(1, 0))

    def test_add(self):
        """Test Complex addition.

        """
        # Complex number addition
        self.assertEqual(self.c1 + self.c2, pmath.Complex(3, 1))
        self.assertEqual(self.c2 + self.c1, pmath.Complex(3, 1))

        # Complex and real addition
        self.assertEqual(self.c2 + 1, pmath.Complex(3, -1))
        self.assertEqual(1 + self.c2, pmath.Complex(3, -1))

    def test_sub(self):
        """Test Complex subtraction.

        """
        # Complex number subtraction
        self.assertEqual(self.c1 - self.c2, pmath.Complex(-1, 3))
        self.assertEqual(self.c2 - self.c1, pmath.Complex(1, -3))

        # Complex and real subtraction
        self.assertEqual(self.c2 - 1, pmath.Complex(1, -1))
        self.assertEqual(1 - self.c2, pmath.Complex(-1, 1))

    def test_mul(self):
        """Test Complex multiplication.

        """
        # Complex multiplication
        self.assertEqual(self.c1 * self.c2, pmath.Complex(4, 3))
        self.assertEqual(self.c2 * self.c1, pmath.Complex(4, 3))

        # Test unit multiplication
        self.assertEqual(self.c_real * self.c_imag, pmath.Complex(0, 1))
        self.assertEqual(self.c_imag * self.c_real, pmath.Complex(0, 1))

        # Complex and scalar multiplication
        self.assertEqual(self.c1 * 2, pmath.Complex(2, 4))
        self.assertEqual(2 * self.c1, pmath.Complex(2, 4))

    def test_eq(self):
        """Test Complex equality.

        """
        # Complex number equality
        self.assertEqual(self.c1, self.c1)
        self.assertEqual(self.c1, pmath.Complex(1, 2))

        # Complex and real equality
        self.assertEqual(self.c_real, 1)
        self.assertEqual(1, self.c_real)
        self.assertNotEqual(self.c1, 1)
        self.assertNotEqual(1, self.c1)

    def test_io(self):
        """Test Complex I/O.

        """
        self.assertEqual(repr(self.c1), 'pmath.Complex(1, 2)')
        self.assertEqual(repr(eval('pmath.Complex(5, 1)')), 'pmath.Complex(5, 1)')
        self.assertEqual(eval(repr(self.c2)), self.c2)
        self.assertEqual(str(self.c1), '(1, 2)')

if __name__ == '__main__':
    unittest.main()
