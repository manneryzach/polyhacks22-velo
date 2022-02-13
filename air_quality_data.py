import json
import csv

# data_path = "./MTLData/rsqa-indice-qualite-air-station.csv"
data_path = "./MTLData/rsqa-indice-qualite-air-station-historique.csv"

with open(data_path) as csvfile:
    reader = csv.DictReader(csvfile)

    last_date = "lol"
    last_heure = "lol"
    first = True

    date_dict = {}
    hour_dict = {}
    hour_array = []

    not_first = False
    last_date = "lol"
    last_heure = -4
    for row in reader:

        station_id = row['stationId']
        coord = [float(row['longitude']),float(row['latitude'])]
        heure = int(row['heure'])
        date = row['date']
        valeur = row['valeur']
        color = [0, int(255-255*int(valeur)/100),0]

        new_dict = {"station_id":station_id, "coordinates":coord, "valeur":int(valeur),"color":color,}

        if ((last_date != date) and not_first):
            hour_dict[last_heure] = hour_array
            date_dict[last_date] = hour_dict
            hour_array = []
            hour_dict = {}
            hour_array.append(new_dict)

        elif ((heure != last_heure) and not_first):
            hour_dict[last_heure] = hour_array
            hour_array = []
            hour_array.append(new_dict)

        else:
            hour_array.append(new_dict)

        last_date = date
        last_heure = heure
        not_first = True



with open("./Data/air_quality.json", 'w') as f:
    json.dump(date_dict, f)
