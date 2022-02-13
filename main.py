import streamlit as st
from api_calls import *
import page_intro
import page_app

st.set_page_config(
    page_title="VéloViz",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)

layer_select = st.sidebar.container()

img = open('img/bike_cropped_2.svg').read()
layer_select.markdown(img, unsafe_allow_html=True)

if st.session_state.get('about', False):
    page_intro.show_page()
    _, col, _ = st.sidebar.columns([1,1,1])
    col.button("Get Started")
else:
    page_app.show_page()
    st.sidebar.button("About us", key='about')