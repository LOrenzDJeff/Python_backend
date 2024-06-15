from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import io
import base64

app = Flask(__name__)
CORS(app)  # Разрешить CORS для всего приложения

@app.route('/generate_signal')
def generate_signal():
    # Ваш код для генерации данных
    x_min, x_max = -10, 10
    y_min, y_max = -10, 10
    resolution = 1000

    x, y = np.meshgrid(np.linspace(x_min, x_max, resolution), 
                       np.linspace(y_min, y_max, resolution))
    power = np.sqrt(x**2 + y**2)
    cmap = LinearSegmentedColormap.from_list('custom', [(0, 'red'), (0.5, 'yellow'), (1, 'green')])
    
    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
    contour = ax.contourf(x, y, power, levels=20, cmap=cmap, alpha=0.5)
    ax.set_axis_off()
    
    # Сохраняем изображение в буфер
    buf = io.BytesIO()
    fig.savefig(buf, format='svg', transparent=True, bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    
    # Кодирование изображения в Base64
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    
    # Возвращаем изображение в формате Base64
    return jsonify({'imageBase64': img_base64})

if __name__ == '__main__':
    app.run(debug=True)