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

# Bike rack layer

racks_df = pd.read_json("./Data/bike_racks.json")

bike_racks_layer = pdk.Layer(
    "ScatterplotLayer",
    racks_df,
    pickable=True,
    opacity=1,
    stroked=True,
    filled=True,
    radius_scale=1,
    radius_min_pixels=2,
    radius_max_pixels=10,
    line_width_min_pixels=0.5,
    get_position="coordinates",
    get_radius=1,
    get_fill_color=[0, 255, 0],
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
    get_width=1.5,
)

def getLayer():
    layer_dict = {
        "REV": rev_layer,
        "bike_path": normal_path_layer,
        "bixi_stations": bixi_stations_layer,
        "construction_layer": construction_layer,
        "bike_rack_layer":bike_racks_layer,
    }
    return layer_dict


def getPointLayer(lon, lat):
    return pdk.Layer(
        "ScatterplotLayer",
        pickable=True,
        opacity=1,
        stroked=True,
        filled=True,
        radius_scale=1,
        radius_min_pixels=2,
        radius_max_pixels=10,
        line_width_min_pixels=0.5,
        get_position=[lon, lat],
        get_radius=1,
        get_fill_color=[0, 0, 255],
        get_line_color=[0, 0, 0],
    )
