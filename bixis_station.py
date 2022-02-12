import streamlit as st
import pydeck as pdk
import pandas as pd

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

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=45.5017,
         longitude=-73.5673,
         zoom=11,
         pitch=0,
     ),
     layers=[
         bixi_stations_layer,
     ],
 ))
