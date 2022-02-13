import streamlit as st
import pydeck as pdk
import pandas as pd

import getLayers

dates = getLayers.getDates()
heures = getLayers.getHeures()

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=45.5017,
         longitude=-73.5673,
         zoom=11,
         pitch=0,
     ),
     layers=[
         getLayers.getLayer()["air_quality_layer"][dates[0]][heures[0]],
         getLayers.getLayer()["REV"],
     ],
 ))
