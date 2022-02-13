from importlib.resources import read_text
import streamlit as st
from pathlib import Path

def show_page():

    file = 'intro.md'

    for i in range(8):
        st.sidebar.write("")

    intro_markdown = Path(file).read_text()
    st.markdown(intro_markdown)

    return