import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from shapely.affinity import scale, rotate

def create_ellipse(center, width, height, angle):
    ellipse = Point(center).buffer(1)
    ellipse = scale(ellipse, width, height)
    ellipse = rotate(ellipse, angle)
    return ellipse

ellipse1 = create_ellipse((0, 0), 5, 2, 30)
ellipse2 = create_ellipse((2, 1), 5, 2, 60)

boundary1 = LineString(ellipse1.exterior.coords)
boundary2 = LineString(ellipse2.exterior.coords)
intersection = boundary1.intersection(boundary2)

fig, ax = plt.subplots()

x1, y1 = ellipse1.exterior.xy
ax.plot(x1, y1, label='Ellipse 1')

x2, y2 = ellipse2.exterior.xy
ax.plot(x2, y2, label='Ellipse 2')

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
