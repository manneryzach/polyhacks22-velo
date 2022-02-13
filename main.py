from turtle import onclick
import streamlit as st
from api_calls import *
import page_intro
import page_app
from pathlib import Path

layer_select = st.sidebar.container()

img = open('img/bike.svg').read()
layer_select.markdown(img, unsafe_allow_html=True)

if 'about' not in st.session_state:
    st.session_state['about'] = False

if st.session_state['about']:
    page_intro.show_page()
    _, col, _ = st.sidebar.columns([1,1,1])
    col.button("Get Started")
else:
    page_app.show_page()
    st.sidebar.button("About us", key='about')