import streamlit as st
# import pandas as pd
# import numpy as np
import pydeck as pdk
import geocoder
from api_calls import *
from getLayers import getLayer


def show_page():
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Montréal appartient-elle aux cyclistes?</h1>", unsafe_allow_html=True)
    layer_select = st.sidebar.container()

    # img = open('img/bike.svg').read()
    # layer_select.markdown(img, unsafe_allow_html=True)

    layers = getLayer()
    with layer_select:
        '## What would you like to see?'
        for key in layers:
            st.checkbox(key, key=key)

    # Get user current location
    g = geocoder.ip('me')
    lat, lon = g.latlng

    query = st.sidebar.text_input('Search location:', value="--", key="query")

    if query != "--":
        res = query_location(query, lat, lon)

        query_options = st.sidebar.selectbox(
            'Select from:', res, 
            key="query_options"
        )

        [[lon, lat]] = res['center'].loc[res['place_name'] == query_options]
        
        # Add point  
        st.session_state['location'] = True
        # layers["location"] = getPointLayer(lon, lat)

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

    stats = st.empty()

    st.text("Environ __ cyclistes par jour voyagent les rues de Montréal. ")
    
    return