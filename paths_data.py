import json

color_code = {
    "prot" : [41,115,155],
    "sep" : [184,196,128],
    "nulle" : [212,231,158],
}

# Data treatment

def clean_data(input_file, output_file):

    with open(input_file) as f:
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

    with open(output_file, 'w') as f:
        json.dump(new_json, f)

clean_data("./MTLData/reseau-express-velo.json", "./Data/REV_paths.json")
clean_data("./MTLData/reseau_cyclable.json", "./Data/normal_paths.json")
