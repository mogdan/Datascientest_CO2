# cd C:\Dev_Projects\Datascientest_CO2\Datascientest_CO2
# streamlit run streamlit_CO2.py


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Trame du site 

# Titre & Sidebar
st.sidebar.image("C:\Dev_Projects\Datascientest_CO2\streamlit_assets/CO2.png", use_column_width=True)
st.title(":green[Etude sur les émissions de CO2 des Véhicules Particuliers]")

st.sidebar.title(":green[Sommaire]")
pages=["Introduction", "Préparation des données", "Entraînement des modèles", "Conclusion", "Prédictions"]
page=st.sidebar.radio("Aller vers", pages)

st.sidebar.title(":green[Auteurs]")
st.sidebar.markdown("📧 [Olivier BAUDOIN](mailto:baud43@gmail.com)")
st.sidebar.markdown("📧 [Yulia HADDAOU](mailto:yuliahaddadou@yahoo.fr)")
st.sidebar.markdown("📧 [Etienne PETIT](mailto:e.petit16@gmail.com)")
st.sidebar.markdown("📧 [Daniel PHAN](mailto:phan_daniel@ymail.com)")

# Introduction & Sources de données
if page == pages[0] : 
  st.write("### :grey[Introduction]")



# Préparation des données
if page == pages[1] : 
  st.write("### :grey[Préparation des données]")

# Entraînement des modèles
if page == pages[2] : 
  st.write("### :grey[Entraînement des modèles]")

# Conclusion
if page == pages[3] : 
  st.write("### :grey[Conclusion]")

# Prédictions
if page == pages[4] : 
  st.write("### :grey[Prédictions]")