import json
import os

import requests
import folium
import numpy as np
from scipy.spatial import Voronoi
import random
from matplotlib.colors import to_hex

from Bounds import Bounds
from City import City
from Coordinate import Coordinate
from SubwayStation import SubwayStation

API_KEY = "AIzaSyDTPaisXU2C5YpWMZlYM0Uz6oqUQsBiDow"
CACHE_DIR = "cache"


def get_city(city_name: str) -> City:
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": city_name, "key": API_KEY}

    json_filepath = f"{CACHE_DIR}/response_{city_name}.json"
    if os.path.exists(json_filepath):
        print("Using cached city info")
        response = json.loads(open(json_filepath).read())
    else:
        print("Making city info request")
        response = requests.get(url, params=params).json()
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        f = open(json_filepath, "w")
        f.write(json.dumps(response))
        f.close()

    if response["status"] == "OK":
        result = response["results"][0]
        bounds = Bounds(
            Coordinate(result["geometry"]["bounds"]["northeast"]["lat"],
                       result["geometry"]["bounds"]["northeast"]["lng"]),
            Coordinate(result["geometry"]["bounds"]["southwest"]["lat"],
                       result["geometry"]["bounds"]["southwest"]["lng"]),
        )
        location = Coordinate(result["geometry"]["location"]["lat"],
                              result["geometry"]["location"]["lng"])

        return City(city_name, bounds, location)
    else:
        raise Exception(f"Ошибка: {response.get('error_message', 'неизвестная ошибка')}")


def get_subway_stations(city: City) -> (set[SubwayStation], set[Coordinate]):
    STEP = 0.1
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    results = set()
    markers = set()

    lat_min, lng_min = (city.bounds.northeast.lat, city.bounds.northeast.lng)
    lat_max, lng_max = (city.bounds.southwest.lat, city.bounds.southwest.lng)

    if lat_min > lat_max:
        lat_min, lat_max = lat_max, lat_min
    if lng_min > lng_max:
        lng_min, lng_max = lng_max, lng_min

    lat = lat_min
    while lat < lat_max:
        lat += STEP
        lng = lng_min
        while lng < lng_max:
            lng += STEP
    # if True:
    #     if True:
    #         lat, lng = city.location.lat, city.location.lng
            markers.add(Coordinate(lat, lng))
            params = {
                "location": f"{lat},{lng}",
                "radius": 25000,
                "type": "subway_station",
                "key": API_KEY,
            }

            json_filepath = f"{CACHE_DIR}/response_{lat:.5f}_{lng:.5f}.json"
            if os.path.exists(json_filepath):
                print("Using cached stations info")
                response = json.loads(open(json_filepath).read())
            else:
                print("Making stations info request")
                response = requests.get(url, params=params).json()
                if not os.path.exists(CACHE_DIR):
                    os.makedirs(CACHE_DIR)
                f = open(json_filepath, "w")
                f.write(json.dumps(response))
                f.close()

            if response["status"] == "OK":
                for station in [
                    SubwayStation(place["name"],
                                  Coordinate(
                                      place["geometry"]["location"]["lat"],
                                      place["geometry"]["location"]["lng"]
                                  ))
                    for place in response["results"]
                ]:
                    results.add(station)

    return results, markers


def generate_random_color():
    return to_hex(tuple(random.random() for _ in range(3)))


def create_voronoi_map(city: City, stations: set[SubwayStation], markers: set[Coordinate]):
    m = folium.Map(location=[city.location.lat, city.location.lng], zoom_start=12)

    for station in stations:
        folium.Marker(location=[station.location.lat, station.location.lng],
                      icon=folium.Icon(color="red", icon="subway")).add_to(m)

    for marker in markers:
        folium.Marker(location=[marker.lat, marker.lng],
                      icon=folium.Icon(color="green", icon="subway")).add_to(m)

    points = np.array([(station.location.lat, station.location.lng) for station in stations])
    vor = Voronoi(points)

    colors = [generate_random_color() for _ in range(len(vor.regions))]

    for region_idx, color in zip(vor.regions, colors):
        if not -1 in region_idx and region_idx:
            polygon = [vor.vertices[i] for i in region_idx]
            try:
                folium.Polygon(
                    locations=polygon,
                    color=color,
                    weight=1,
                    fill=True,
                    fill_color=color,
                    fill_opacity=0.4
                ).add_to(m)
            except ValueError:
                pass

    return m


if __name__ == "__main__":
    city_name = "Минск"
    # city_name = "Санкт-Петербург"

    city = get_city(city_name)
    stations, markers = get_subway_stations(city)

    for station in stations:
        print(station.name)

    if stations:
        voronoi_map = create_voronoi_map(city, stations, markers)
        voronoi_map.save("voronoi_map_colored.html")
    else:
        print("Станции метро не найдены.")
