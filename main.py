import streamlit as st
# import pandas as pd
# import numpy as np
import pydeck as pdk
import geocoder
from api_calls import *
from getLayers import getLayer
import page_intro as intro
import page_app as app
from importlib.resources import read_text
from pathlib import Path

# title_alignment="""
# <style>
# "How bikeable is Montreal?" {
#   text-align: center
# }
# </style>
# """
# Sidebar page selection

layer_select = st.sidebar.container()

img = open('img/bike.svg').read()
layer_select.markdown(img, unsafe_allow_html=True)

pages = {
        "Introduction": intro,
        "Bike info": app,
    }

st.sidebar.title("Options")

# Radio buttons to select desired option
page = st.sidebar.radio("", tuple(pages.keys()))

pages[page].show_page()


about_file = "about.md"

about = Path(about_file).read_text()
st.sidebar.markdown(about)
