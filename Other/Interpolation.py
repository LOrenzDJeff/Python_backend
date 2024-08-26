import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Данные для cellid = 139956839
'''
latitudes = np.array([55.0294739, 55.0294739, 55.0294739, 55.0294739, 55.0294739, 
             55.0294784, 55.0294784, 55.0294693, 55.0294693, 55.0294693,
             55.0294713, 55.0294713, 55.0294814, 55.0294814, 55.0294813,
             55.0294812, 55.0294918, 55.0294918])
longitudes = np.array([83.026856, 83.026856, 83.026856, 83.026856, 83.026856,
              83.0268714, 83.0268714, 83.0268725, 83.0268725, 83.0268725,
              83.0268745, 83.0268745, 83.0268516, 83.0268516, 83.0268732,
              83.0268729, 83.0269253, 83.0269253])
rsrp = np.array([-109, -109, -111, -111, -111, -110, -110, -109, -109, -109,
               -108, -108, -112, -112, -112, -112, -109, -109])

'''
data = [
    {"Latitude:": 55.0134451, "Longitude:": 82.9505132, "Rsrp:": -72},
    {"Latitude:": 55.0134172, "Longitude:": 82.9502775, "Rsrp:": -78},
    {"Latitude:": 55.0133529, "Longitude:": 82.9500039, "Rsrp:": -80},
    {"Latitude:": 55.0133393, "Longitude:": 82.9496564, "Rsrp:": -79},
    {"Latitude:": 55.0131527, "Longitude:": 82.9495720, "Rsrp:": -78},
    {"Latitude:": 55.0130006, "Longitude:": 82.9493610, "Rsrp:": -76},
    {"Latitude:": 55.0128176, "Longitude:": 82.9494080, "Rsrp:": -83},
    {"Latitude:": 55.0127992, "Longitude:": 82.9497845, "Rsrp:": -85},
    {"Latitude:": 55.0128814, "Longitude:": 82.9500132, "Rsrp:": -75},
    {"Latitude:": 55.0130531, "Longitude:": 82.9502686, "Rsrp:": -73},
    {"Latitude:": 55.0133704, "Longitude:": 82.9505603, "Rsrp:": -70},
]

# Извлечение данных
latitudes = np.array([d["Latitude:"] for d in data])
longitudes = np.array([d["Longitude:"] for d in data])
rsrp = np.array([d["Rsrp:"] for d in data])

# Определяем минимальное и максимальное значения RSRP
min_rsrp = -120
max_rsrp = -70

center_latitude = np.mean(latitudes)
center_longitude = np.mean(longitudes)

# Создание сетки для интерполяции
grid_lat, grid_lon = np.mgrid[min(latitudes):max(latitudes):100j, min(longitudes):max(longitudes):100j]

# Интерполяция
grid_rsrp = griddata((latitudes, longitudes), rsrp, (grid_lat, grid_lon), method='linear')

# Установление границ для цветовой карты
grid_rsrp = np.clip(grid_rsrp, min_rsrp, max_rsrp)

# Построение графика
plt.figure(figsize=(10, 10))
contour = plt.imshow(grid_rsrp.T, extent=(min(longitudes), max(longitudes), min(latitudes), max(latitudes)),
                     origin='lower', cmap='RdYlGn_r', alpha=0.6, vmin=min_rsrp, vmax=max_rsrp)

# Удаление осей
plt.axis('off')

# Сохранение изображения
output_path = 'coverage_map.png'
plt.savefig(output_path, bbox_inches='tight', pad_inches=0, transparent=True)
plt.close()

print(center_latitude, center_longitude)