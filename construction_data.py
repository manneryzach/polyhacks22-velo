import json
import lxml
import xml.etree.ElementTree as ET

data_path = "./MTLData/info_travaux.kml"

tree = ET.parse(data_path)
root = tree.getroot()

# print([elem.tag for elem in root.iter()])
# {http://www.opengis.net/kml/2.2}coordinates

new_json = []

counter = 1
for coords in root.iter('{http://www.opengis.net/kml/2.2}coordinates'):
    coords = coords.text.replace('\n0','').replace("0\n",'')
    coords_s = coords.split(',')

    coords_s = list(filter(None, coords_s))
    path = []

    # print(len(coords_s) if (len(coords_s)%2 == 0) else "~")
    for i in range(0, int(len(coords_s)/2), 2):
        new_coord = [float(coords_s[i]), float(coords_s[i+1])]
        path.append(new_coord)

    data_dict = {"name":str(counter),"color":[250,199,72],"path":path}
    new_json.append(data_dict)

    # print(coords_s)
    # print(path)
    # print("~-~-~-~")
    counter+=1

with open("./Data/construction.json", 'w') as f:
    json.dump(new_json, f)
