import streamlit as st
import pandas as pd
import numpy as np


# titre du site
st.set_page_config(layout='wide', page_icon="https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Green_co2_logo2.png?raw=true")
col1, col2, col3 = st.columns([1, 10, 1])
col2.title(":blue[Etude sur les émissions de CO₂ des véhicules particuliers]")

# menu gauche de navigation
st.sidebar.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Car_co2_light.png?raw=true", use_column_width=True)
st.sidebar.title("Sommaire")
# accès aux pages du site
pages=["1 - Exploration", "2 - Data Preparation", "3 - Modélisation", "4 - Conclusion"]
page=st.sidebar.radio("Aller vers la page :", pages)

# contenu de la page sélectionnée
if page == pages[0]: 
  st.header('1 - Exploration des datasets', divider=True)
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

  st.markdown("# :grey[Conclusion Analyse Exploratoire]")

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


elif page == pages[1]:
  st.header('2 - Nettoyage et sélection des données', divider=True)
  
elif page == pages[2]:
  st.header('3 - Modélisation', divider=True)
  
elif page == pages[3]:
  st.header('4 - Conclusion', divider=True)
  st.markdown("""
              Pour conclure notre étude sur les émission de CO2 des véhicules, plusieurs points clés émergent:
              - **Données limitées** : Nous avons exploitéles données disponibles depuis 2015, mais leur recul est restreint.
              - **Surreprésentation des véhicules thermiques** : Notre jeu de données est largement composé de vehicules essence et diesel, ce qui reflète la forte présence de ces motorisation sur les routes.
              - **Variables influentes pour le rejet de CO2** : Le dimensionnement du véhicules( poids, taille de la cylindrée) et les spécifications du moteur se sont avérés plus significatifs pour prédire les émissions de CO2.
  """)
  st.subheader("Tableau des Perspectives d'Amélioration")
  # Créer les colonnes pour structurer le tableau
  col1, col2 = st.columns([1, 2])
  # Ajouter le contenu dans chaque colonne
  with col1:
    st.subheader("Domaine")
    st.write("1. Standardisation des mesures")
    st.write("2. Modèles d'apprentissage")
    st.write("3. Étude sur les conditions")
  with col2:
    st.subheader("Piste d'amélioration")
    st.write("1. Uniformiser les données d'émission de CO₂ pour toutes les marques, y compris les véhicules plus récents.")
    st.write("2. Utiliser des modèles avancés avec optimisation des hyperparamètres pour améliorer la précision.")
    st.write("3. Intégrer des données sur les conditions de circulation (rurale, urbaine, mixte) pour affiner les prédictions.")
 
  from sklearn.preprocessing import StandardScaler
  from sklearn.decomposition import PCA
  from sklearn.cluster import KMeans
  from sklearn.neighbors import KNeighborsRegressor
  from sklearn.model_selection import train_test_split
  import joblib


  # Chargement du dataset
  df = pd.read_csv('https://raw.githubusercontent.com/mogdan/Datascientest_CO2/refs/heads/main/streamlit_assets/Dataset_Rendu2_cleaned.csv', sep=',')

  # Liste des colonnes catégorielles
  col_cat = ['Type_approval_number', 'Type', 'Variant', 'Make', 'Commercial_name', 'Category_vehicle_type_approved', 'Fuel_mode', 'Fuel_type'] 

  # Application de l'encodage fréquentiel pour chaque colonne catégorielle
  for col in col_cat:
    freq_encoding = df[col].value_counts() / len(df)
    df[col] = df[col].map(freq_encoding)

  # Sélection des variables explicatives (X) et de la variable cible (Y)
  Y = df['CO2_Emissions']
  X = df.drop(['CO2_Emissions'], axis=1)

  # Standardisation des données
  scaler = StandardScaler()
  X_norm = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

  # Clustering avec KMeans (optionnel, pour clustering visuel)
  kmeans_model = KMeans(n_clusters=5, random_state=42)
  X_norm['cluster'] = kmeans_model.fit_predict(X_norm)

  # Réduction dimensionnelle avec PCA
  pca = PCA(n_components=2)
  principalComponents = pca.fit_transform(X_norm.drop('cluster', axis=1))

  # Combinaison PCA et KMeans dans un DataFrame
  X_combined = pd.DataFrame(data=principalComponents, columns=['Component 1', 'Component 2'])
  X_combined['Cluster'] = X_norm['cluster']

  # Division en ensembles d'entraînement et de test
  X_train, X_test, Y_train, Y_test = train_test_split(X_combined[['Component 1', 'Component 2']], Y, test_size=0.2, random_state=42)

  # Entraînement du modèle KNN
  knn = KNeighborsRegressor(n_neighbors=4)
  knn.fit(X_train, Y_train)

  # Sauvegarde du modèle KNN et PCA avec joblib
  joblib.dump(knn, 'model_knn.joblib')
  joblib.dump(scaler, 'scaler.joblib')
  joblib.dump(pca, 'pca.joblib')

  # Chargement des modèles KNN et transformateurs (scaler et PCA)
  model_knn = joblib.load('model_knn.joblib')
  scaler = joblib.load('scaler.joblib')
  pca = joblib.load('pca.joblib')


  # Titre de l'application
  st.title("Application de calcul des émissions de CO2")
  st.header("Calculateur d'empreinte carbone pour les véhicules")

  # Choix du pays (simplifié ici avec un seul exemple)
  emission_factors = {"France": {"transportation": 28.7}}
  st.subheader("Votre pays")
  country = st.selectbox("Sélectionnez votre pays", ["France"])

  # Mise en page avec colonnes
  col1, col2, col3 = st.columns(3)

  # Distance parcourue
  with col1:
    st.subheader("🚗Distance parcourue (km/j)")
    daily_distance = st.slider("Distance", 0.0, 100.0, 10.0)
    yearly_distance = daily_distance * 365  # Conversion en distance annuelle

  # Type de carburant
  with col2:
    st.subheader("⛽Type de carburant")
    fuel_type = st.selectbox("Carburant", ["PETROL", "DIESEL", "LPG", "PETROL/ELECTRIC", "DIESEL/ELECTRIC", 'NG', 'E85', 'NG-BIOMETHANE'])

  # Cylindrée du moteur
  with col3:
    st.subheader( "🏎️💨Taille de la cylindrée (en L)")
    engine_capacity = st.slider("Cylindrée", 0.0, 10.0, 1.6)

  # Année de construction
  reporting_year = st.number_input("📅Année de référence pour la prédiction", min_value=2017, max_value=2022, step=1)

  # Encodage fréquentiel pour le type de carburant
  fuel_type_freq = df['Fuel_type'].value_counts() / len(df)
  fuel_type_encoded = fuel_type_freq.get(fuel_type, 0)  # Par défaut, valeur de fréquence zéro si absent

  # Calcul des émissions
  if st.button("Calculer les émissions de CO2"):
    # Créer une liste de caractéristiques avec valeurs par défaut pour celles qui manquent
    prediction_input = [reporting_year, yearly_distance, engine_capacity, fuel_type_encoded]
    
    # Ajouter des valeurs par défaut (0) pour les caractéristiques manquantes
    # Supposons que le modèle a été entraîné avec 14 caractéristiques
    nombre_caracteristiques_attendues = 14
    if len(prediction_input) < nombre_caracteristiques_attendues:
        prediction_input += [0] * (nombre_caracteristiques_attendues - len(prediction_input))

    # Restructurer en tableau 2D pour l'entrée du scaler
    prediction_input = [prediction_input]  # Encapsuler dans une liste pour former un tableau 2D

    # Appliquer les transformations
    prediction_input_scaled = scaler.transform(prediction_input)  # Maintenant, prediction_input est un tableau 2D
    prediction_input_pca = pca.transform(prediction_input_scaled)

    # Prédiction des émissions
    CO2_emission = model_knn.predict(prediction_input_pca)[0]
    CO2_emission = round(CO2_emission, 2)

    # Affichage des résultats
    st.header("Résultats")
    st.info(f"Émissions estimées pour {yearly_distance} km par an : {CO2_emission} tonnes de CO2 par an")

    # Empreinte carbone totale
    with col3:
        st.subheader("Empreinte carbone totale")
        st.info(f"Total des émissions : {CO2_emission} tonnes de CO2 par an")

  # Affichage de la limite moyenne par habitant
  st.warning("La limite maximale moyenne est de 282,963 tonnes de CO2 par habitant")



