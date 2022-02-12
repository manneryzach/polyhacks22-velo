import pydeck as pdk
import pandas as pd

# Bixi Layer

bixi_df = pd.read_json("./Data/bixi_stations.json")

bixi_stations_layer = pdk.Layer(
    "ScatterplotLayer",
    bixi_df,
    pickable=True,
    opacity=1,
    stroked=True,
    filled=True,
    radius_scale=1,
    radius_min_pixels=2,
    radius_max_pixels=10,
    line_width_min_pixels=0.5,
    get_position="coordinates",
    get_radius="capacity",
    get_fill_color=[255, 0, 0],
    get_line_color=[0, 0, 0],
)

# Path layers

rev_df = pd.read_json("./Data/REV_paths.json")
normal_df = pd.read_json("./Data/normal_paths.json")

rev_layer = pdk.Layer(
    type="PathLayer",
    data=rev_df,
    pickable=True,
    get_color="color",
    width_scale=10,
    width_min_pixels=1,
    get_path="path",
    get_width=0.5,
)

normal_path_layer = pdk.Layer(
    type="PathLayer",
    data=normal_df,
    pickable=True,
    get_color="color",
    width_scale=10,
    width_min_pixels=1,
    get_path="path",
    get_width=0.5,
)

# Construction Layer

construction_df = pd.read_json("./Data/construction.json")

construction_layer = pdk.Layer(
    type="PathLayer",
    data=construction_df,
    pickable=True,
    get_color="color",
    width_scale=10,
    width_min_pixels=1,
    get_path="path",
    get_width=0.5,
)

def getLayer():
    layer_dict = {
        "REV": rev_layer,
        "bike_path": normal_path_layer,
        "bixi_stations": bixi_stations_layer,
        "construction_layer": construction_layer,
    }
    return layer_dict
