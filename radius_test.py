import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Задаем параметры
x_min, x_max = -10, 10
y_min, y_max = -10, 10
resolution = 1000

# Создаем сетку координат
x, y = np.meshgrid(np.linspace(x_min, x_max, resolution), 
                   np.linspace(y_min, y_max, resolution))

# Вычисляем мощность сигнала
power = np.sqrt(x**2 + y**2)

# Создаем пользовательскую цветовую карту
cmap = LinearSegmentedColormap.from_list('custom', [(0, 'red'), (0.5, 'yellow'), (1, 'green')])

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(10, 10), dpi=100)

# Отрисовываем радиус мощности сигнала с пользовательской цветовой картой
contour = ax.contourf(x, y, power, levels=20, cmap=cmap, alpha=0.5)

# Убираем оси и название
ax.set_axis_off()

# Сохраняем в прозрачном формате SVG
fig.savefig('signal_power_radius.svg', transparent=True, bbox_inches='tight', pad_inches=0)
