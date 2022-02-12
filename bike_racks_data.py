import pydeck as pdk
import pandas as pd

data_path = "./MTLData/supportvelosigs.csv"

with open(data_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # //
