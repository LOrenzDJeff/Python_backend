import json
from network import from_go, send_to_client
from geometry import find_m, find_radius, create_circle, distance, get_intersections, get_closest_pair
from plot import plot_circles_and_intersections
from utils import m_to_grad

Novlon = 82.946912
Novlat = 55.010810

char, addr = from_go()

circles = []
print(char)
for item in char:
    x, y = find_m(item[1], item[0], Novlon, Novlat)
    rad = find_radius(item[2]) / 1000
    circles.append(create_circle((x, y), rad))

intersections = get_intersections(circles)

if len(intersections) >= 2:
    closest_pair, min_dist = get_closest_pair(intersections)
    print(f"Близкие друг к другу точки ({closest_pair[0].x:.2f}, {closest_pair[0].y:.2f}) и ({closest_pair[1].x:.2f}, {closest_pair[1].y:.2f}) растояние между ними {min_dist:.2f}")
else:
    closest_pair = None
    print("Нет точек")

plot_circles_and_intersections(circles, intersections, closest_pair)

if closest_pair:
    midx = (closest_pair[0].x + closest_pair[1].x) / 2
    midy = (closest_pair[0].y + closest_pair[1].y) / 2  
    lat, lon = m_to_grad(midx, midy, Novlon, Novlat)
    result = {'latitude': lat, 'longitude': lon}
   # send_to_client(result, addr)
