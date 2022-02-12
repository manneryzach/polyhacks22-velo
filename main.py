import streamlit as st
# import pandas as pd
# import numpy as np
import pydeck as pdk
import geocoder
from api_calls import *

# token = 'pk.eyJ1IjoiY2FybGt0IiwiYSI6ImNremswbGFxbzExbG8ybnBhMGc4aTRxNjAifQ.eO1vcS0sYVskxH8FWG_mnQ'


st.title('How bikeable is Montreal?')
layer_select = st.sidebar.container()
    
with layer_select:
    '## What would you like to see?'
    bike_layer = st.checkbox('Bike lanes')
    air_layer = st.checkbox('Air quality')
    topo_layer = st.checkbox('Topography')

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

# Draw map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=11,
        pitch=0,
    )
))