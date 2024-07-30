import matplotlib.pyplot as plt
from shapely.geometry import Point

def create_circle(center, radius):
    circle = Point(center).buffer(radius)
    return circle

circle1 = create_circle((0, 0), 5)
circle2 = create_circle((4, 0), 5)

boundary1 = circle1.boundary
boundary2 = circle2.boundary
intersection = boundary1.intersection(boundary2)

fig, ax = plt.subplots()

x1, y1 = circle1.exterior.xy
ax.plot(x1, y1, label='Circle 1')

x2, y2 = circle2.exterior.xy
ax.plot(x2, y2, label='Circle 2')

if intersection.is_empty:
    print("No intersection")
else:
    points = []
    if intersection.geom_type == 'MultiPoint':
        points = list(intersection.geoms)
    elif intersection.geom_type == 'Point':
        points = [intersection]
    
    for pt in points:
        ax.plot(pt.x, pt.y, 'ro')
        print(f"Intersection at: ({pt.x:.2f}, {pt.y:.2f})")

ax.set_aspect('equal', 'box')
plt.legend()
plt.show()
