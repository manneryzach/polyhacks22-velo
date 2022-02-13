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

    layers = getLayer()
    with layer_select:
        '## What would you like to see?'
        for key in layers:
            st.checkbox(key, key=key)

    # Get user current location
    g = geocoder.ip('me')
    lat, lon = g.latlng

    search = st.sidebar.empty()
    query = search.text_input('Search location:', value="--", key="query")

    if query != "--":
        res = query_location(query, lat, lon)
        # Add default option
        df = res.append({'place_name':"--", 'center': [lon, lat]}, ignore_index=True)

        query = search.text_input('Search location:', value="--", key="query2")

        query_options = search.selectbox(
            'Select location:', df, 
            key="query_options"
        )
        st.write(query_options)
        st.write(query)
        # st.stop()

        [[lon, lat]] = df['center'].loc[df['place_name'] == query_options]

        if query_options == "--":
            query = search.text_input('Search location:', value="--", key="query3")


    # def reset_loc():
    #     lat, lon = g.latlng
    # st.button("Reset", on_click=reset_loc)

    map_container = st.empty()
    # col1, col2, col3 = map_container.columns([1,1,1])
    # button = col2.button("Get started")
    # if button:

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