import streamlit as st
# import pandas as pd
# import numpy as np
import pydeck as pdk
import geocoder
from api_calls import *
from getLayers import getLayer

st.title('How bikeable is Montreal?')
layer_select = st.sidebar.container()

layers = getLayer()
with layer_select:
    '## What would you like to see?'
    for key in layers:
        st.checkbox(key, key=key)

# Get user current location
g = geocoder.ip('me')
lat, lon = g.latlng

search = st.sidebar.text_input('Search location:')
if search != "":
    res = query_location(search, lat, lon)
    query_options = st.sidebar.selectbox(
        "", res
    )
    [[lon, lat]] = list(res['center'].loc[res['place_name'] == query_options])

# def reset_loc():
#     lat, lon = g.latlng
# st.button("Reset", on_click=reset_loc)

map_container = st.empty()
# col1, col2, col3 = map_container.columns([1,1,1])
# button = col2.button("Get started")
# if button:

# Draw map
map_container.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=11,
        pitch=0,
    ),
    layers=[
        layer for layer_name, layer in layers.items()
        if st.session_state[layer_name]
    ]
))