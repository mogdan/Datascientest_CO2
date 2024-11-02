import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# titre du site
st.set_page_config(layout='wide', page_icon='static/green_co2_logo2.png')
col1, col2, col3 = st.columns([1, 10, 1])
col2.title(":blue[Etude sur les émissions de CO₂ des véhicules particuliers]")

# menu gauche de navigation
st.sidebar.image('static/Car_co2_light.png', use_column_width=True)
st.sidebar.title("Sommaire")
# accès aux pages du site
pages=["1 - Exploration", "2 - Data Preparation", "3 - Modélisation"]
page=st.sidebar.radio("Aller vers la page :", pages)

# contenu de la page sélectionnée
if page == pages[0]: 
  st.header('1 - Exploration des datasets', divider=True)
  st.markdown("""
  #### Sources de données suggérées :
  > -	Source **ADEME «[ data.gouv.fr](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_) »** : caractéristiques techniques des véhicules commercialisés en **France** entre 2001 et 2015, ainsi que les consommations de carburant, les émissions de CO2 et les émissions de polluants dans l’air (**300K lignes**)
  > -	Source **« [eea.europa.eu](https://www.eea.europa.eu/data-and-maps/data/co2-cars-emission-20) »** : caractéristiques et émissions de CO2 de toutes les voitures immatriculées  chaque année en **Europe** entre 2010 et 2023 (**80M lignes**)
 
  Ces deux sources de données représentent le **flux** des nouveaux véhicules entrants sur le marché (soit français, soit européen)
  
  #### Datasets complémentaires explorés :
  > - Données Critair concernant le marché français
  > -	Données de circulation en France et à Paris
  > -	Parc (**stock**) des véhicules en France par an de 2011 à 2023 ([Source SDES](https://www.statistiques.developpement-durable.gouv.fr/389-millions-de-voitures-en-circulation-en-france-au-1er-janvier-2023))
  > -	Emissions de CO2 déduites des consommations réelles de carburant collectées sur le terrain sur les véhicules des particuliers en 2021 (Source : [Agence Européenne de l’Environnement](https://climate.ec.europa.eu/news-your-voice/news/collecting-real-world-data-co2-emissions-and-fuel-consumption-new-cars-and-vans-2021-03-05_en?prefLang=fr) - EEA)
              """)
  

elif page == pages[1]:
  st.header('2 - Nettoyage et sélection des données', divider=True)

else:
  st.header('3 - Modélisation', divider=True)

