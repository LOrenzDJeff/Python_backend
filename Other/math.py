import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
from itertools import combinations

def find_radius(RSRP):
    h = 60
    f = 3.6
    Ptx = 41    
    Prx = RSRP + 10 * np.log10(600)
    PL = Ptx - Prx
    m = (PL - 28 - 20 * np.log10(f)) / 22
    radius = (10 ** (m))
    radius = np.sqrt(radius ** 2 - h ** 2)
    print(f"radius = {radius:.10f} m")
    return radius

def m_to_grad(x, y, oldx, oldy):
    lat = oldx + ((180 * x) / (6371 * np.cos(55 * np.pi / 180) * np.pi))
    lon = oldy + ((180 * y) / (6371 * np.pi))
    print(f"lat = {lat:.10f}, lon = {lon:.10f}")
    return lat, lon

def grad_to_m(x, y):
    xkm = (6371 * np.cos(55 * np.pi / 180) * x * np.pi) /  180
    ykm = (6371 * y * np.pi) /  180
    return xkm, ykm
    
def find_m(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    x,y = grad_to_m(x, y)
    return x, y

def create_circle(center, radius):
    circle = Point(center).buffer(radius)
    return circle

def distance(point1, point2):
    return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

Novlon = 82.946912
Novlat = 55.010810

RSRP1 = -72
RSRP2 = -73
RSRP3 = -73

lat1 = 55.0134451
lon1 = 82.9505132
lat2 = 55.0134172
lon2 = 82.9502775
lat3 = 55.0133529
lon3 = 82.9500039

rad1 = find_radius(RSRP1) / 1000
rad2 = find_radius(RSRP2) / 1000
rad3 = find_radius(RSRP3) / 1000

x, y = find_m(lon1, lat1, Novlon, Novlat)
x2, y2 = find_m(lon2, lat2, Novlon, Novlat)
x3, y3 = find_m(lon3, lat3, Novlon, Novlat)

circles = [
    create_circle((x, y), rad1),
    create_circle((x2, y2), rad2),
    create_circle((x3, y3), rad3)
]

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
                
if len(intersections) >= 2:
    min_dist = float('inf')
    closest_pair = None
    for point1, point2 in combinations(intersections, 2):
        dist = distance(point1, point2)
        if dist < min_dist:
            min_dist = dist
            closest_pair = (point1, point2)
    print(f"Близкие друг к другу точки ({closest_pair[0].x:.2f}, {closest_pair[0].y:.2f}) и ({closest_pair[1].x:.2f}, {closest_pair[1].y:.2f}) растояние между ними {min_dist:.2f}")
else:
    print("Нет точек")   


fig, ax = plt.subplots()

for i, circle in enumerate(circles):
    x, y = circle.exterior.xy
    ax.plot(x, y, label=f'Circle {i+1}')

for pt in intersections:
    ax.plot(pt.x, pt.y, 'ro')

if closest_pair:
    ax.plot(closest_pair[0].x, closest_pair[0].y, 'bo', markersize=10)  
    ax.plot(closest_pair[1].x, closest_pair[1].y, 'bo', markersize=10)

ax.set_aspect('equal', 'box')
plt.legend()
plt.show()

midx = (closest_pair[0].x + closest_pair[1].x) / 2
midy = (closest_pair[0].y + closest_pair[1].y) / 2

m_to_grad(midx, midy, Novlon, Novlat)