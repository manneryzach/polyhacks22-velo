import json
from gbfs.client import GBFSClient

DATA_URL = "https://gbfs.velobixi.com/gbfs/gbfs.json"

client = GBFSClient(DATA_URL, 'en')

stations = client.request_feed('station_information').get('data').get('stations')

new_json = []
for station in stations:
    station_id = station["station_id"]
    capacity = station["capacity"]
    coords = [float(station["lon"]),float(station["lat"])]
    name = station['name']

    new_dict = {"name": name, "id": station_id, "coordinates":coords, "capacity":int(capacity)}
    new_json.append(new_dict)

with open("./Data/bixi_stations.json", 'w') as f:
    json.dump(new_json, f)

