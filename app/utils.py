import svgwrite
from io import BytesIO

def calculate_radius(rsrp):
    max_rsrp = -60
    min_rsrp = -120
    max_radius = 1000
    min_radius = 100

    if (rsrp > max_rsrp):
        return min_radius
    if (rsrp < min_rsrp):
        return max_radius

    return min_radius + (max_radius - min_radius) * (min_rsrp - rsrp) / (min_rsrp - max_rsrp)

def calculate_approx_location(data):
    total_lat = sum([d['latitude'] for d in data])
    total_lon = sum([d['longitude'] for d in data])
    avg_lat = total_lat / len(data)
    avg_lon = total_lon / len(data)
    return avg_lat, avg_lon

def create_svg(radius):
    dwg = svgwrite.Drawing(size=(1000, 1000))
    center = (500, 500)
    circle = dwg.circle(center=center, r=radius, fill='blue', fill_opacity=0.3)
    dwg.add(circle)
    output = BytesIO()
    dwg.write(output)
    output.seek(0)
    return output.getvalue().decode()
