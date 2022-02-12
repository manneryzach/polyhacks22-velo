import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

'# How bikeable is Montreal?'
layer_select = st.sidebar.container()
    
with layer_select:
    '## What would you like to see?'
    bike_layer = st.checkbox('Bike lanes')
    air_layer = st.checkbox('Air quality')
    topo_layer = st.checkbox('Topography')

st.map()