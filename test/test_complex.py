import unittest
from core import pmath
import math


class TestComplex(unittest.TestCase):
    """Test the Complex math class.

    TODO: Enrich test cases
    """

    def setUp(self):
        """Setup the common test data, including the following complex numbers:
            z1 = 1 + 2i
            z2 = 2 - 1i
            z_real = 1 + 0i (Real)
            z_imag = 0 + 1i (Imaginary)
        """
        self.z1 = pmath.Complex(1, 2)
        self.z2 = pmath.Complex(2, -1)
        self.z_real = pmath.Complex(1, 0)
        self.z_imag = pmath.Complex(0, 1)
        return None

    def test_getter(self):
        """Test getter methods."""
        self.assertEqual(self.z1.real, 1)
        self.assertEqual(self.z1.imaginary, 2)

    def test_setter(self):
        """Test setter methods."""
        self.z1.real = 2
        self.assertEqual(self.z1.real, 2)
        self.z1.imaginary = 3
        self.assertEqual(self.z1.imaginary, 3)

    def test_conjugate(self):
        """Test computation of complex conjugation."""
        self.assertEqual(self.z1.conjugate(), pmath.Complex(1, -2))
        self.assertEqual(self.z_real.conjugate(), self.z_real)
        self.assertEqual(self.z_imag.conjugate(), -self.z_imag)

    def test_magnitude(self):
        """Test computation of the complex magnitude."""
        self.assertEqual(self.z1.magnitude2(), pmath.Complex(5, 0))
        self.assertEqual(self.z1.magnitude(), pmath.Complex(math.sqrt(5), 0))
        self.assertEqual(self.z2.magnitude(), pmath.Complex(math.sqrt(self.z2.magnitude2().real), 0))
        self.assertEqual(self.z_real.magnitude2(), pmath.Complex(1, 0))
        self.assertEqual(self.z_imag.magnitude2(), pmath.Complex(1, 0))

    def test_add(self):
        """Test Complex addition."""
        # Complex number addition
        self.assertEqual(self.z1 + self.z2, pmath.Complex(3, 1))
        self.assertEqual(self.z2 + self.z1, pmath.Complex(3, 1))

        # Complex and real addition
        self.assertEqual(self.z2 + 1, pmath.Complex(3, -1))
        self.assertEqual(1 + self.z2, pmath.Complex(3, -1))

    def test_sub(self):
        """Test Complex subtraction."""
        # Complex number subtraction
        self.assertEqual(self.z1 - self.z2, pmath.Complex(-1, 3))
        self.assertEqual(self.z2 - self.z1, pmath.Complex(1, -3))

        # Complex and real subtraction
        self.assertEqual(self.z2 - 1, pmath.Complex(1, -1))
        self.assertEqual(1 - self.z2, pmath.Complex(-1, 1))

    def test_mul(self):
        """Test Complex multiplication."""
        # Complex multiplication
        self.assertEqual(self.z1 * self.z2, pmath.Complex(4, 3))
        self.assertEqual(self.z2 * self.z1, pmath.Complex(4, 3))

        # Test unit multiplication
        self.assertEqual(self.z_real * self.z_imag, pmath.Complex(0, 1))
        self.assertEqual(self.z_imag * self.z_real, pmath.Complex(0, 1))

        # Complex and scalar multiplication
        self.assertEqual(self.z1 * 2, pmath.Complex(2, 4))
        self.assertEqual(2 * self.z1, pmath.Complex(2, 4))

    def test_div(self):
        """Test Complex division."""
        # Complex division
        self.assertEqual(self.z1 / self.z2, pmath.Complex(0, 1), "z1/z2")
        self.assertEqual(self.z2 / self.z1, pmath.Complex(0, -1), "z2/z1")

        # Complex and scalar division
        self.assertEqual(self.z1 / 2., pmath.Complex(0.5, 1), "z2/2")
        self.assertEqual(2. / self.z1, pmath.Complex(0.4, -0.8), "2/z2")

    def test_eq(self):
        """Test Complex equality."""
        # Complex number equality
        self.assertEqual(self.z1, self.z1)
        self.assertEqual(self.z1, pmath.Complex(1, 2))

        # Complex and real equality
        self.assertEqual(self.z_real, 1)
        self.assertEqual(1, self.z_real)
        self.assertNotEqual(self.z1, 1)
        self.assertNotEqual(1, self.z1)

    def test_polar(self):
        """Test polar coordinates."""
        # Magnitude
        self.assertEqual(self.z_imag.r, 1)
        self.assertEqual(self.z_real.r, 1)

        # Phase
        self.assertEqual(self.z_imag.phi, math.pi/2.)
        self.assertEqual(self.z_real.phi, 0.)

    def test_sort(self):
        """Test sorting of complex numbers."""
        # Comparison
        self.assertEqual(self.z1 < self.z2, True)
        self.assertEqual(self.z2 < self.z1, False)
        self.assertEqual(self.z_imag < self.z_real, True)
        self.assertEqual(self.z_real < self.z_imag, False)

        # Sort operation
        self.assertEqual(sorted([self.z1, self.z2]),[self.z1, self.z2])
        self.assertEqual(sorted([self.z2, self.z1]),[self.z1, self.z2])

    def test_io(self):
        """Test Complex I/O."""
        self.assertEqual(repr(self.z1), 'pmath.Complex(1.0, 2.0)')
        self.assertEqual(repr(eval('pmath.Complex(5, 1)')), 'pmath.Complex(5.0, 1.0)')
        self.assertEqual(eval(repr(self.z2)), self.z2)
        self.assertEqual(str(self.z1), '(1.0, 2.0)')


if __name__ == '__main__':
    unittest.main()
