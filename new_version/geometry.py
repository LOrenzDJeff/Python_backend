from shapely.geometry import Point
from shapely.ops import unary_union
from itertools import combinations
import numpy as np
from utils import find_m, find_radius

def create_circle(center, radius):
    circle = Point(center).buffer(radius)
    return circle

def distance(point1, point2):
    return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def get_intersections(circles):
    intersections = []
    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            boundary1 = circles[i].boundary
            boundary2 = circles[j].boundary
            intersection = boundary1.intersection(boundary2)
            if not intersection.is_empty:
                if intersection.geom_type == 'MultiPoint':
                    intersections.extend(list(intersection.geoms))
                elif intersection.geom_type == 'Point':
                    intersections.append(intersection)
    return intersections

def get_closest_pair(intersections):
    min_dist = float('inf')
    closest_pair = None
    for point1, point2 in combinations(intersections, 2):
        dist = distance(point1, point2)
        if dist < min_dist:
            min_dist = dist
            closest_pair = (point1, point2)
    return closest_pair, min_dist
