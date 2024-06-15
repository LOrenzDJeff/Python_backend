import requests
from flask import current_app
from .utils import calculate_approx_location, calculate_radius, create_svg

def get_station_data():
    response = requests.get(current_app.config['GO_API_URL'])
    data = response.json()

    result = []
    for station_data in data["stations"]:
        lat, lon = calculate_approx_location(station_data["measurements"])
        avg_rsrp = sum([d['rsrp'] for d in station_data["measurements"]]) / len(station_data["measurements"])
        radius = calculate_radius(avg_rsrp)
        svg_image = create_svg(radius)
        result.append({
            "id": station_data["id"],
            "latitude": lat,
            "longitude": lon,
            "radius": radius,
            "svg": svg_image
        })

    return result
