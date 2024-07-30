import unittest
import numpy as np
from utils import find_radius, m_to_grad, grad_to_m, find_m

class TestUtils(unittest.TestCase):

    def test_find_radius(self):
        self.assertAlmostEqual(find_radius(-80), 2657.5800655, places=7)
        self.assertAlmostEqual(find_radius(-100), 26.5758007, places=7)
        
    def test_find_radius_invalid(self):
        with self.assertRaises(ValueError):
            find_radius('invalid')

    def test_m_to_grad(self):
        lat, lon = m_to_grad(1000, 1000, 82.946912, 55.010810)
        self.assertAlmostEqual(lat, 82.9559274, places=7)
        self.assertAlmostEqual(lon, 55.0197449, places=7)

    def test_grad_to_m(self):
        xkm, ykm = grad_to_m(1, 1)
        self.assertAlmostEqual(xkm, 57.2859927, places=7)
        self.assertAlmostEqual(ykm, 111.1949266, places=7)
        
    def test_find_m(self):
        x, y = find_m(82.9559274, 55.0197449, 82.946912, 55.010810)
        self.assertAlmostEqual(x, 1000, places=7)
        self.assertAlmostEqual(y, 1000, places=7)

if __name__ == '__main__':
    unittest.main()
