import streamlit as st
import pydeck as pdk
import pandas as pd

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

normal_layer = pdk.Layer(
    type="PathLayer",
    data=normal_df,
    pickable=True,
    get_color="color",
    width_scale=10,
    width_min_pixels=1,
    get_path="path",
    get_width=0.5,
)

# Test HTML
# view_state = pdk.ViewState(latitude=37.782556, longitude=-122.3484867, zoom=10)

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=45.5017,
         longitude=-73.5673,
         zoom=11,
         pitch=0,
     ),
     layers=[
         rev_layer,
         normal_layer,
     ],
 ))

# Test HTML
# r = pdk.Deck(layers=[rev_layer], initial_view_state=view_state, tooltip={"text": "{name}"})
# r.to_html("path_layer.html")
