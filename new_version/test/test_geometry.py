import unittest
from shapely.geometry import Point
from geometry import create_circle, distance, get_intersections, get_closest_pair

class TestGeometry(unittest.TestCase):

    def test_create_circle(self):
        center = (0, 0)
        radius = 1
        circle = create_circle(center, radius)
        self.assertTrue(circle.contains(Point(0.5, 0.5)))
        self.assertFalse(circle.contains(Point(2, 2)))

    def test_distance(self):
        point1 = Point(0, 0)
        point2 = Point(3, 4)
        self.assertEqual(distance(point1, point2), 5)

    def test_get_intersections(self):
        circle1 = create_circle((0, 0), 1)
        circle2 = create_circle((1, 0), 1)
        intersections = get_intersections([circle1, circle2])
        self.assertEqual(len(intersections), 2)

    def test_get_closest_pair(self):
        point1 = Point(0, 0)
        point2 = Point(3, 4)
        point3 = Point(6, 8)
        intersections = [point1, point2, point3]
        closest_pair, min_dist = get_closest_pair(intersections)
        self.assertEqual(closest_pair, (point1, point2))
        self.assertEqual(min_dist, 5)

if __name__ == '__main__':
    unittest.main()
