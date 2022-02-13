import streamlit as st
from api_calls import *
import page_intro
import page_app
from pathlib import Path

layer_select = st.sidebar.container()

img = open('img/bike.svg').read()
layer_select.markdown(img, unsafe_allow_html=True)

pages = {
        "Introduction": page_intro,
        "Bike info": page_app,
    }


# Radio buttons to select desired option
page = st.sidebar.radio("", tuple(pages.keys()))

st.sidebar.title("Options")

pages[page].show_page()

st.sidebar.markdown(open("about.md").read())
