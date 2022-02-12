import json

data_path = "./MTLData/supportvelosigs.csv"

with open(data_path) as f:
    lines = f.readlines()

    coords = []
    for line in lines:
        line = line.split(",")

        new_coord = []
        # print(line)
        for elem in line:
            try:
                # print(float(elem))
                if (float(elem) >= -75 and float(elem) <= -70):
                    # print(float(elem))
                    new_coord.append(float(elem))
                elif (float(elem) >= 45 and float(elem) <= 46):
                    # print(float(elem))
                    new_coord.append(float(elem))
                    coords.append(new_coord)
                    new_coord = []
            except:
                pass

    # print(coords)

new_json = []
counter = 1
for coord in coords:
    new_dict = {"name":str(counter),"coordinates":coord}
    new_json.append(new_dict)

with open('./Data/bike_racks.json','w') as f2:
    json.dump(new_json, f2)
