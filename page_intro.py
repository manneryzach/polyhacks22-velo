from PIL import Image
import streamlit as st

def show_page():

    file = 'intro.md'

    for i in range(8):
        st.sidebar.write("")

    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>VéloViz: Montréal sur Vélo!</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2.5,1])

    col1.markdown("<h2 style='text-align: left; color: #B71111;'>Pourquoi VéloViz?</h2>", unsafe_allow_html=True)
    col1.write("""
        Selon Vélo Quebec, les Montréalais passent un total de 3 640 000 heures par semaine sur leurs vélos et 740 000 personnes les utilisent comme mode de transport. Sachant ceci, nous voulions créer une application qui améliore l'accessibilité au cyclisme en région métropolitaine.
    """)
    
    image = Image.open('img/cool_biker.jpg')
    col2.header(" ")
    col2.image(image, width=400)
    
    col1, col2 = st.columns([2,4])
    col2.markdown("<h2 style='text-align: left; color: #B71111;'>Que fait notre application?</h2>", unsafe_allow_html=True)
    col2.write("Notre application permet de facilement visualiser toutes les données importantes pour un(e) cycliste à Montréal, telles que les pistes cyclables, les zones de construction, les stations de BIXI et autres!")

    image = Image.open('img/finally.jpg')
    col1.header(" ")
    col1.image(image, width=400)


    st.markdown("<h2 style='text-align: left; color: #B71111;'>L'avenir de VéloViz</h2>", unsafe_allow_html=True)

    st.write("Nous aimerions ajouter d'autres données importantes, telles que les vols par région ainsi que les zones propices à accidents. La touche finale serait de faire en sorte que nos données soient constamment mises à jour (real-time data).")

    return