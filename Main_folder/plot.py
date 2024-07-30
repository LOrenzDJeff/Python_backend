import matplotlib.pyplot as plt

def plot_circles_and_intersections(circles, intersections, closest_pair):
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
