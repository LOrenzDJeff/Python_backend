import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Задаем параметры
x_min, x_max = -200, 200
y_min, y_max = -200, 200
resolution = 400
initial_rsrp = -60

# Создаем сетку координат
x, y = np.meshgrid(np.linspace(x_min, x_max, resolution), 
                   np.linspace(y_min, y_max, resolution))

# Вычисляем мощность сигнала
distance = np.sqrt(x**2 + y**2)


n = 2
rsrp = initial_rsrp - 10 * n * np.log10(distance + 1e-6)

# Создаем пользовательскую цветовую карту
cmap = LinearSegmentedColormap.from_list('custom', [(0, 'red'), (0.5, 'yellow'), (1, 'green')])

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(4, 4), dpi=100)

# Отрисовываем радиус мощности сигнала с пользовательской цветовой картой
contour = ax.contourf(x, y, rsrp, levels=20, cmap=cmap, alpha=0.5)

# Убираем оси и название
ax.set_axis_off()

# Сохраняем в прозрачном формате SVG
fig.savefig('signal_power_radius.svg', transparent=True, bbox_inches='tight', pad_inches=0)

plt.show()