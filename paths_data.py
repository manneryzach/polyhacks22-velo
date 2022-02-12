import json

# Data treatment

color_code = {
    "prot" : [41,115,155],
    "sep" : [184,196,128],
    "nulle" : [212,231,158],
}

with open("./MTLData/reseau-express-velo.json") as f:
    data = json.load(f)

features = data["features"]

new_json = []

counter = 1
for feature in features:
    properties = feature["properties"]
    # print(properties["LONGUEUR"])

    geometry = feature["geometry"]
    path = geometry["coordinates"][0]
    protected_4S = properties["PROTEGE_4S"]
    separateur = properties["SEPARATEUR"]
    if (protected_4S == "OUI"):
        color = color_code["prot"]
    elif (separateur):
        color = color_code["sep"]
    else:
        color = color_code["nulle"]

    data_dict = {"name": str(counter), "color": color, "path": path}
    new_json.append(data_dict)
    counter+=1

with open("./Data/REV_paths.json", 'w') as f:
    json.dump(new_json, f)
