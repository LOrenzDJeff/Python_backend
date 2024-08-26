import json
import matplotlib.pyplot as plt

with open('thermalmapdataall (2).json', 'r') as f:
    data = json.load(f)

fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
fig.patch.set_alpha(0.0)
coordinates = []
radius = 0.001
for item in data:
    #coordinates.append((float(item['longitude']), float(item['latitude'])))
    center = (float(item['longitude']), float(item['latitude']))
    circle_artist = plt.Circle(center, radius)
    ax.add_artist(circle_artist)
    
    
ax.set_xlim(82, 84)
ax.set_ylim(54, 56)
plt.axis('off')
# Показ полотна
plt.savefig('test.png', transparent=True)
plt.close()
#print(coordinates)