import streamlit as st
# import pandas as pd
# import numpy as np
import pydeck as pdk
import geocoder
from api_calls import *
from getLayers import getLayer, getPointLayer


def show_page():
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Montréal appartient-il aux cyclistes?</h1>", unsafe_allow_html=True)
    layer_select = st.sidebar.container()

    layers = getLayer()
    with layer_select:
        '## What would you like to see?'
        for key in layers:
            st.checkbox(key, key=key)

    # Get user current location
    # g = geocoder.ip('me')
    # lat, lon = g.latlng
    lat, lon = 45.5017, -73.5673

    query = st.sidebar.text_input('Cherchez un endroit:', value="--", key="query")

    if query != "--":
        res = query_location(query, lat, lon)

        query_options = st.sidebar.selectbox(
            'Select from:', res, 
            key="query_options"
        )

        [[lon, lat]] = res['center'].loc[res['place_name'] == query_options]
        
        # Add point  
        # st.session_state['location'] = True
        # layers["location"] = getPointLayer(lat, lon)

    map_container = st.empty()

    # Draw map
    map_container.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
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

    return
