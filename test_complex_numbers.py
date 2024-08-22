import unittest
from complex_numbers import *

class TestComplexNumbers(unittest.TestCase):

    def test_add_complex(self):
        self.assertEqual(add_complex((1, 2), (3, 4)), (4, 6))
        self.assertEqual(add_complex((-1, -2), (-3, -4)), (-4, -6))

    def test_sub_complex(self):
        self.assertEqual(sub_complex((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(sub_complex((-1, -2), (-3, -4)), (2, 2))

    # Agrega más pruebas para las otras funciones...

if __name__ == '__main__':
    unittest.main()
