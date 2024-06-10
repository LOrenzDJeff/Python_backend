import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import calculation as calc

def visualize_signals(signals):
    # Список для хранения геометрий точек и радиусов
    points = []
    radii = []

    for signal in signals:
        location = signal['location']
        rspr = signal['rspr']
        radius = calc.calculate_signal_radius(rspr)
        
        # Преобразуем координаты в объект Point
        point = Point(location.x, location.y)
        points.append(point)
        radii.append(radius)

    # Создаем GeoDataFrame
    gdf = gpd.GeoDataFrame({'geometry': points, 'radius': radii})

    # Создаем график
    fig, ax = plt.subplots()
    gdf.plot(ax=ax, color='blue')

    # Рисуем круги, представляющие радиусы сигналов
    for point, radius in zip(points, radii):
        circle = plt.Circle((point.x, point.y), radius, color='red', fill=False)
        ax.add_patch(circle)

    plt.show()