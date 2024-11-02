# cd C:\Dev_Projects\Datascientest_CO2\Datascientest_CO2
# streamlit run streamlit_CO2.py


import streamlit as st
import pandas as pd
import numpy as np

# Trame du site 

# Titre & Sidebar
url_image_CO2="https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/CO2.png?raw=true"
st.sidebar.image(url_image_CO2, use_column_width=True)
st.title(":green[Etude sur les émissions de CO2 des Véhicules Particuliers]")

st.sidebar.title(":green[Sommaire]")
pages=["Introduction", "Préparation des Données", "Entraînement des Modèles", "Conclusion de l'étude", "Prédictions"]
page=st.sidebar.radio("Aller vers", pages)

st.sidebar.title(":green[Auteurs]")
st.sidebar.markdown("📧 [Olivier BAUDOIN](mailto:baud43@gmail.com)")
st.sidebar.markdown("📧 [Yulia HADDAOU](mailto:yuliahaddadou@yahoo.fr)")
st.sidebar.markdown("📧 [Etienne PETIT](mailto:e.petit16@gmail.com)")
st.sidebar.markdown("📧 [Daniel PHAN](mailto:phan_daniel@ymail.com)")

# Introduction & Sources de données
if page == pages[0] : 
  st.markdown("# :grey[Prise en main du sujet]")

  with st.expander("Problématique"):
    problematique = '''
    L’**accumulation de gaz à effet de serre** dans l’atmosphère est l’une des principales causes de réchauffement climatique. Or, les transports, et principalement la voiture, sont la première source de gaz à effet de serre en France . Il est donc important de connaître l’empreinte carbone de son véhicule afin de pouvoir réduire son impact sur l’environnement. 

    Parmi les transports privilégiés par les Français, la voiture occupe une place de choix. En effet, selon l’ADEME, les Français se déplacent à :green[**77% en voiture**] contre :
    -	11% en train ;
    -	8,8% en transport en commun ;
    -	1,8% en avion ;
    -	1,6% en deux roues motorisées.

    La voiture est donc responsable d’une part importante de notre empreinte carbone dans notre quotidien. Face à l’urgence climatique, certains constructeurs ont déjà œuvré ces dix dernières années sur l’amélioration des rendements des moteurs thermiques, l’aérodynamisme et l’allègement des voitures pour limiter l’impact environnemental. 

    Intéressés par cette problématique, nous avons ainsi choisi ce sujet pour mettre à profit nos nouvelles compétences en tant que Data Analyst. 

    Les objectifs pour notre équipe sur ce sujet sont les suivants :
    -	:green[**Consolider les données d’étude**] : Rechercher, analyser et nettoyer les données à notre disposition sur ce périmètre auprès de plusieurs sources de données
    -	:green[**Concevoir un modèle de prédiction**] :  pour déterminer les émissions de CO2 en fonction des caractéristiques du véhicule
  
    '''
    st.markdown(problematique)

  with st.expander("Sources des Données"):
      ademe = '''
      **[Source ADEME](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/)**  
      Données allant de 2002 jusqu’à 2015, uniquement sur les immatriculations françaises, avec un nombre de variables variant chaque année (en incluant les noms des variables aussi). En volume de data, toutes ces années représentent 300K lignes.
      '''
      st.markdown(ademe)

      ue = '''
      **[Source UE](https://www.eea.europa.ea/data-and-maps/data/co2-cars-emission-20)**  
      Données provenant d’une seule et même source de 2010 à 2022 (données finales) et 2023 (données prévisionnelles). Ces données relatent le nombre d’immatriculations faites par pays dans l’UE avec toutes les caractéristiques véhicules complémentaires. Concernant le volume, nous sommes aux alentours de 80 millions de lignes entre 2010 et 2023.
      '''
      st.markdown(ue)

      st.markdown("Pour résumer, ces deux sources de données représentent le flux des nouveaux véhicules entrants sur le marché (soit français, soit européen)")

  with st.expander("Autres Sources Disponibles"):
      otherSources = '''
      Nous avons par ailleurs exploré d’autres sources de données pour venir enrichir les données de base que nous avions : 
      -	Récupération des données Crit’air concernant le marché français
      -	Données de circulation en France et à Paris
      -	Parc (stock) des véhicules en France par an de 2011 à 2023 (Source SDES)
      -	Emissions de CO2 déduites des consommations réelles de carburant collectées sur le terrain sur les véhicules des particuliers en 2021 (ces données ont été collectées pour permettre une analyse comparative avec les données théoriques constructeurs présentes dans les fichiers ADEME et UE. Source : [Agence Européenne de l’Environnement](https://climate.ec.europa.eu/news-your-voice/news/collecting-real-world-data-co2-emissions-and-fuel-consumption-new-cars-and-vans-2021-03-05_en?prefLang=fr) - EEA)
      '''
      st.markdown(otherSources)

  st.markdown("# :grey[Choix des données]")
  with st.expander("Modalités"):
        modalites = '''
        :green[**Cette étape a pour enjeu de nous permettre de sélectionner la source de données la plus pertinente pour démarrer notre étude**]. 

        Durant cette étape, notre approche fut d’apprécier la qualité des données au travers des scopes suivants :
        -	La cohérence 
        -	La validité 
        -	La complétude
        -	La précision 
        -	La disponibilité 
        -	L’actualité 

        '''
        st.markdown(modalites)

  with st.expander("Données ADEME"):      
        st.markdown("L‘illustration suivante permet de se rendre compte de la qualité macro des données ADEME :")
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/ademe_raw.png?raw=true", use_column_width=True)

        ademe_choice = '''
        Pour chaque fichier est indiqué :
        -	Le nb de lignes
        -	Le nb / titres des colonnes

        Notre analyse est alors la suivante :
        -	**Niveau cohérence** : disparités fortes au niveau du format des données
        -	**Niveau complétude** : pour certaines années il manque de la donnée (2004). Il y a également des très fortes disparités du nombre d’entrées entre les années

        '''
        st.markdown(ademe_choice)

  with st.expander("Données UE"):      
        st.markdown("Au niveau des données UE, nous constatons rapidement que nous sommes sur un set de données déjà standardisées sur le périmètre européen de 2010 à 2023. ")
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/ue_raw.png?raw=true", use_column_width="auto")
        
        ue_choice = '''
        Notre analyse est alors la suivante :
        -	**Niveau cohérence** : les données sont déjà standardisées dans un même format
        -	**Niveau complétude** : il y a également sur ce set de données des écarts importants sur les enregistrements entre certaines années
        -	**Niveau actualité** : ces données semblent être à jour
        '''
        st.markdown(ue_choice)

  st.markdown("# :grey[Conclusion de l'analyse exploratoire]")

  with st.expander("Choix des données"):      
        st.markdown("Au vu de la disparité des données sur les fichiers ADEME et de leur ancienneté, nous avons décidé de nous concentrer sur les :green[**données UE.**] ")
  
  with st.expander("Choix de la période d'observation"):      
        period_choice = '''
        :green[**Cette étape a pour enjeu de nous permettre de sélectionner la plage de données sur laquelle va s’appuyer notre modèle.**]
        
        Pour notre étude, nous avons choisi la période « 2017 – 2022 ».
        -	Notre 1ère intention fut de garder l’année 2015 pour permettre une analyse comparative données UE / ADEME. Cependant le faible volume de données a exclu ce choix par la suite
        -	Les données relatives aux années 2010 à 2014 ont également été exclues du fait du faible volume de données
        -	L’année 2023 a également été exclue car elle représente des données non finalisées
        '''
        st.markdown(period_choice)
             

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