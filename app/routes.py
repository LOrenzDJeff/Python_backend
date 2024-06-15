from flask import jsonify
from .services import get_station_data

def register_routes(app):
    @app.route('/approximate_stations', methods=['GET'])
    def get_approximate_stations():
        stations = get_station_data()
        return jsonify(stations)

# Регистрация маршрутов при создании приложения
def init_app(app):
    register_routes(app)
