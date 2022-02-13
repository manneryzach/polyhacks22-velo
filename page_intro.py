from PIL import Image
import streamlit as st

def show_page():

    file = 'intro.md'

    for i in range(8):
        st.sidebar.write("")

    st.title("VéloViz: Montréal sur Vélo!")
    
    col1, col2 = st.columns([10,2])

    col1.header("Qui nous sommes")
    col1.write("""
        Selon Vélo Quebec, les Montréalais passent un total de 3 640 000 heures par semaine sur leurs vélos et 740 000 personnes les utilisent comme mode de transport. En temps que cyclistes, il est important de se questioner: Il y a-t-il moyen d'améliorer l'accessibilité ...?
    """)
    
    image = Image.open('img/cool_biker.jpg')
    col2.header(" ")
    col2.image(image, width=400)
    
    col1, col2 = st.columns([2,4])
    col2.header("How we built it")
    col2.write("Text here")

    image = Image.open('img/finally.jpg')
    col1.header(" ")
    col1.image(image, width=200)


    st.header("What's next:")

    st.write("Text here")

    # _, col, _ = st.columns([1,1,1])
    # col.button("Get started")
    return