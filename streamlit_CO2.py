import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import joblib

# titre du site
st.set_page_config(layout='wide', page_icon="https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Green_co2_logo2.png?raw=true")
col1, col2, col3 = st.columns([1, 10, 1])
col2.title(":blue[Etude sur les émissions de CO₂ des véhicules particuliers]")

# menu gauche de navigation
# st.sidebar.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Car_co2_light.png?raw=true", use_column_width=True)
st.sidebar.image("streamlit_assets/Cine_cars_vintage.jpg", use_column_width=True)
st.sidebar.title("Sommaire")
# accès aux pages du site
pages=["1 - Analyse exploratoire ", "2 - Data Preparation", "3 - Modélisation", "4 - Conclusion"]
page=st.sidebar.radio("Aller vers la page :", pages)

# # chargement des données et entraînement aux modèles
# # Chargement du dataset
# df = pd.read_csv('https://raw.githubusercontent.com/mogdan/Datascientest_CO2/refs/heads/main/streamlit_assets/Dataset_Rendu2_cleaned.csv', sep=',')

# # Liste des colonnes catégorielles
# col_cat = ['Type_approval_number', 'Type', 'Variant', 'Make', 'Commercial_name', 'Category_vehicle_type_approved', 'Fuel_mode', 'Fuel_type'] 

# # Application de l'encodage fréquentiel pour chaque colonne catégorielle
# for col in col_cat:
#   freq_encoding = df[col].value_counts() / len(df)
#   df[col] = df[col].map(freq_encoding)

# # Sélection des variables explicatives (X) et de la variable cible (Y)
# Y = df['CO2_Emissions']
# X = df.drop(['CO2_Emissions'], axis=1)

# # Standardisation des données
# scaler = StandardScaler()
# X_norm = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# # Clustering avec KMeans (optionnel, pour clustering visuel)
# kmeans_model = KMeans(n_clusters=5, random_state=42)
# X_norm['cluster'] = kmeans_model.fit_predict(X_norm)

# # Réduction dimensionnelle avec PCA
# pca = PCA(n_components=2)
# principalComponents = pca.fit_transform(X_norm.drop('cluster', axis=1))

# # Combinaison PCA et KMeans dans un DataFrame
# X_combined = pd.DataFrame(data=principalComponents, columns=['Component 1', 'Component 2'])
# X_combined['Cluster'] = X_norm['cluster']

# # Division en ensembles d'entraînement et de test
# X_train, X_test, Y_train, Y_test = train_test_split(X_combined[['Component 1', 'Component 2']], Y, test_size=0.2, random_state=42)

# # Entraînement du modèle KNN
# knn = KNeighborsRegressor(n_neighbors=4)
# knn.fit(X_train, Y_train)

# # Sauvegarde du modèle KNN et PCA avec joblib
# joblib.dump(knn, 'model_knn.joblib')
# joblib.dump(scaler, 'scaler.joblib')
# joblib.dump(pca, 'pca.joblib')

# contenu des pages sélectionnées
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

  st.markdown("# :grey[Consolidation des données]")

  with st.expander("Corrélation des données"):      
        st.markdown("Pour commencer le travail exploratoire, nous avons décidé de faire un heatmap pour regarder les corrélations entre les valeurs numériques. Pou_r se faire, nous avons choisi de remplacer les NaN par la moyenne dans chaque variable.")
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Heatmap.png?raw=true", use_column_width="auto")
        
        corr_model = '''
        Sur ce graphique, 3 corrélations supérieures à 80% peuvent être observées :
        -	**Mt avec m (kg)** : ces 2 variables représentent le poids des véhicules. Il est donc logique qu’elles soient corrélées.
        -	**Enedc (g/km) avec Ewltp (g/km)** : Ces 2 variables représentent les émissions de CO2 calculées avec des normes différentes. Il y a forte corrélation entre les deux ce qu’il s’avère plutôt logique.
        -	**M (kg) avec At2 (mm)** : La variable At2 représente la distance entre les 2 roues AV ou AR d’un véhicule, tout comme l’At1 d’ailleurs. Après une rapide analyse, on remarque que la variable At2 avait plus de NaN que sa consœur et que notre remplacement par la moyenne ait pu avoir des effets de bord.
        '''
        st.markdown(corr_model)

  with st.expander("Analyses des critères ENEDC / EWLTP"):  
        critere = '''
        Ayant observé une corrélation suffisante entre ces 2 critères décrivant les émissions de CO2, nous nous sommes penchés sur l’analyse comparative de ces 2 critères :
        -	**NEDC** signifiant « New European Driving Cycle » ou « Nouveau Cycle de Conduite Européen », c’est une norme d’homologation des véhicules neufs introduite en 1997 en Europe et qui a eu cours jusqu'en septembre 2017. La norme va définir les conditions dans lesquelles un modèle est testé, allant de la vitesse à la température, avec un avantage : tous les véhicules suivent le même protocole.
        -	**WLTP** (Worldwide Harmonized Light Vehicles Test Procedure) pour tout nouveau modèle à partir du 1er septembre 2017. Il concerne tous les véhicules neufs au 1er septembre 2018, et jusqu’aux véhicules en stock homologués NEDC et vendus après le 1er septembre 2019.
        '''
        st.markdown(critere)
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Comparaison ENEDC-EWLTP par an.png?raw=true", use_column_width="auto")
        
        critere1 = '''
        Grâce à cette analyse, c'est à cette étape que nous avons choisi d'exclure les années 2015 et 2016 dans la suite de notre étude à cause du faible nombre de données.
        
        Sur les autres années, notre analyse a été la suivante :
        -	En 2017 et 2018, nous avons des données ENEDC et peu voire pas de données EWLTP
        -	En revanche cette tendance qui s’inverse à partir 2021 où les données ENEDC sont majoritairement absentes.
        -	Durant la période 2019 – 2020, il y a coexistence des données sur ces 2 types de mesures.

        Pour pousser notre analyse d'un cran supplémentaire, nous nous sommes concentrés sur l'année 2020 où nous avons des données complètes sur les 2 critères. 
        '''
        st.markdown(critere1)
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Boxplot - comparasion 2020 ENEDC-EWLTP.png?raw=true", use_column_width="auto")
        critere2 = '''
        Ce que nous avons voulu mettre en évidence ici est la médiane des émissions par type de carburant et par norme (Enedc puis Ewltp), et la différence par type de carburant.

        :green[**Conclusion** : grâce à ce graphique, npous pouvons confirmer que les émissions calculées avec la norme NEDC sont plus faibles qu’avec la norme WLTP.]

        '''
        st.markdown(critere2)

  with st.expander("Analyses de la distribution par type de carburant"):  
        distrib = '''
        Pour continuer notre travail exploratoire, nous avons regardé le nombre de véhicules par type de carburant sur ce jeu de données.
        '''
        st.markdown(distrib)
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Nb véhicules par type de carburant.png?raw=true", use_column_width="auto")
        
        distrib1 = '''
        :green[Nous observons ainsi une grande prédominance des voitures Essence et Diesel dans nos données.]
        
        Pour compléter ce graphique, il nous a semblé intéressant d’observer l’évolution dans le temps pour chaque carburant :
        '''
        st.markdown(distrib1)
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Nb véhicules par type de carburant et par an.png?raw=true", use_column_width="auto")
        distrib2 = '''
        
        :green[Nous observons une diminution progressive des immatriculations pour les voitures Essence / Diésel ces dernières années et une augmentation progressive des voitures électriques à partir de 2019. Cependant, ces graphiques ne permettent pas d’observer de causes conjoncturelles ou structurelles pour ces tendances.]

        Pour aller plus loin, on s'est intéressé à la distribution par type de carburant et la taille de cylindrée pour voir comment sont répartis les véhicules.
        Pour cela, nous avons fait un travail préalable sur la variable **ec (cm3)** où nous avons remplacé les NaN par la médiane calculée

        '''
        st.markdown(distrib2)
        st.image("https://github.com/mogdan/Datascientest_CO2/blob/main/streamlit_assets/Distribution par type de carburant et taille de cylindrée.png?raw=true", use_column_width="auto")
        
        distrib3 = '''
        Nous pouvons voir pour les catégories qui nous intéressent :
        -	**Essence :** Les véhicules essences sont en général bien équilibrées dans leur répartition, la moyenne se situant quasi au même niveau que la médiane. Il y a toutefois une large dispersion de VA (grosses cylindrées – ex. sport, luxe)
        -	**Diesel :** la cylindrée est en général plus importante que pour l’homologue en version essence et possède une dispersion plus faible de valeurs aberrantes.
        '''
        st.markdown(distrib3)


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

  with st.expander("Choix de la norme pour le calcul des émissions"):      
        emission_choice = '''
        Nous avons donc choisi, pour conserver une cohérence temporelle des données d’émissions, de compenser la sous-évaluation des émissions de CO2 par la méthode NEDC en lui ajoutant, pour chaque type de carburant (hors électrique/hydrogène), la médiane de la différence avec les valeurs WLTP mesurée sur 2020.
        
        :green[**Dans notre modèle, nous créerons une nouvelle variable nommée ‘Emissions CO2’ qui prendra la valeur de EWLTP quand elle sera présente et la valeur de ENEDC compensée en l’absence de valeur EWLTP.**]

        :green[**Cette variable sera notre variable cible.**]
        '''
        st.markdown(emission_choice)

elif page == pages[1]:
  st.header('2 - Nettoyage et sélection des données', divider=True)

  with st.expander("Etapes de transformation"):  
   st.markdown('''
               Voici, en résumé, quelles étapes nous allons procéder afin de préparer les données à la modélisation : 
               -	Conserver les données entre 2017 et 2022
               -	Conserver les données FR
               -  Conserver les véhicules avec énergies carbonnées
               -	Conserver les champs suivants : 'Tan', 'T', 'Va', 'Mk', 'Cn', 'Ct', 'm (kg)', 'Enedc (g/km)', 'Ewltp (g/km)', 'W (mm)', 'At1 (mm)', 'Ft', 'Fm', 'ec (cm3)', 'ep (KW)', 'year'
               -	Standardiser la variable 'Mk' (constructeur)
               -	Standardiser la variable 'Ft' (carburant)
               -  Supprimer les doublons
                -	Créer une nouvelle variable 'CO2_Emission' sur la base de 'enedc', 'ewltp' et 'median'
               -	Supprimer les variables ayant permis de construire CO2_Emission
               -  Traitement des NaN
               -	Renommer les titres de colonne pour faciliter la manipulation des données
               ''')
   
  st.markdown("# :grey[Réduction des variables]")
   
  with st.expander("Variable Year"):
   st.markdown("Comme expliqué dans l'analyse exploratoire, :green[**nous devons garder seulement les données entre 2017 et 2022**]")
   st.code("df=df[(df.year>2016) & (df['year']<2023)]")           

  with st.expander("Variables Country"):
   st.markdown("Nous avons fait le choix pour cette étude de garder seulement :green[**les véhicules immatriculés en France**]")
   st.code("df=df[(df['Country']=='FR')]")     

  with st.expander("Variables Fuel type (ft)"):
   st.markdown("Les véhicules électriques ou avec un moteur à hydrogène ne dégageant pas d'émissions de CO2, nous les avons exclus du modèle")
   st.code( '''
            df = df[df['Ft'] != 'ELECTRIC']
            df = df[df['Ft'] != 'HYDROGEN']
            ''')       
   
  with st.expander("Conservation des variables essentielles"):
   st.markdown("Le but de notre étude est de montrer les caractéristiques moteurs émettant du CO2. Nous avons gardé seulement les champs pertinents, qui ont peu de NaN")
   st.markdown('''De plus, une colonne ID est présente dans les données de base, variable que nous avons décidé de supprimer, car nous n'analyserons pas le nombre de véhicules par type de carburant.
               Cela présentera un avantage non négligeable : :green[**une réduction drastique du volume de données**]''')
   st.code( '''
            values_to_keep=['Tan', 'T', 'Va', 'Mk', 'Cn', 'Ct', 'm (kg)', 'Enedc (g/km)', 'Ewltp (g/km)', 'W (mm)', 'At1 (mm)', 'Ft', 'Fm', 'ec (cm3)', 'ep (KW)', 'year']
            df=df[values_to_keep]
            ''')       
  st.markdown("# :grey[Standardisation des variables]")
  with st.expander("Variable Constructeur (Mk)"):
   st.markdown("Beaucoup de champs n'étant pas propres sur cette variable, il a fallu nettoyer les données.")
   st.code( '''
            df['Mk']= df['Mk'].astype(str)
            df['Mk']= df['Mk'].apply(lambda x : x.upper())
            df['Mk'].replace({  'ALPINA':'BMW',
                    'BMW I':'BMW',
                    'QUATTRO' : 'AUDI',
                    'PÃ–SSL' :'PÖSSL',
                    'P?SSL' : 'PÖSSL',
                    'ROLLS ROYCE' : 'ROLLS-ROYCE',
                    'VOLKSWAGEN, VW' : 'VOLKSWAGEN',
                    'MITSUBISHI MOTORS (THAILAND)' : 'MITSUBISHI',
                    'MERCEDES-AMG' : 'MERCEDES AMG',
                    'MERCEDES-BENZ' : 'MERCEDES BENZ',
                    'MC LAREN' : 'MCLAREN',
                    'FORD-CNG-TECHNIK' : 'FORD',
                    'MERCEDES AMG' : 'MERCEDES BENZ',
                    'HYUNDAI                                           ': 'HYUNDAI',
                    'RENAULT TECH' : 'RENAULT'
                 }, inplace=True)
            ''')       
  with st.expander("Variable Fuel type (ft)"):
   st.markdown("Idem pour cette variable.")
   st.code( '''
            df['Ft']= df['Ft'].astype(str)
            df['Ft']= df['Ft'].apply(lambda x : x.upper())
            df['Ft'].replace({'DIESEL-ELECTRIC':'DIESEL/ELECTRIC',
            'UNKNOWN':np.nan,
            'PETROL-ELECTRIC':'PETROL/ELECTRIC', 'NAN':np.nan}, inplace=True)
            ''')       
   
  st.markdown("# :grey[Suppression des doublons]")
  with st.expander("Traitement"):
   st.code( '''
            print("Nombre de lignes AVANT traitement :", len(df))
            print("doublons AVANT traitement: ",df.duplicated().sum())
            df.drop_duplicates(inplace= True)
            print("doublons APRES traitement: ",df.duplicated().sum())
            print("Nombre de lignes APRES traitement :", len(df))
           ''')
   st.markdown('''
              Voici le résultat :
              - Nombre de lignes AVANT traitement : 11463387
              - doublons AVANT traitement:  11232814
              - doublons APRES traitement:  0
              - Nombre de lignes APRES traitement : 230573
               ''')

  st.markdown("# :grey[Création de la variable CO2_Emission]")
  with st.expander("Calcul des médianes pour chaque type de carburant à partir de 'Enedc (g/km)' et 'Ewltp (g/km)'"):
    st.code( '''
            medians_enedc = df.groupby('Ft')['Enedc (g/km)'].median()
            medians_ewltp = df.groupby('Ft')['Ewltp (g/km)'].median()
           ''')
  with st.expander("Fonction pour calculer CO2_Emission"):
    st.markdown('Création de la fonction :')
    st.code( '''
            def calculate_emissions(row):
              if not np.isnan(row['Ewltp (g/km)']):
                return row['Ewltp (g/km)']
              else:
                fuel_type = row['Ft']
                median_enedc = medians_enedc.get(fuel_type, 0)
                median_ewltp = medians_ewltp.get(fuel_type, 0)
                adjustment = median_enedc - median_ewltp
                return row['Enedc (g/km)'] - adjustment
           ''') 
    st.markdown('Avec sa mise en application sur les données')
    st.code('''df['CO2_Emissions'] = df.apply(calculate_emissions, axis=1)''')

    st.markdown('''Suppression des colonnes d'origine''')
    st.code('''df=df.drop(['Enedc (g/km)', 'Ewltp (g/km)'],axis=1)''')

  st.markdown("# :grey[Traitement des NaN]")
  with st.expander("Choix du traitement"):
    st.markdown('''
                Nous avons calculé à cette étape le nombre de NaN dans les données restantes, voici le résultat :
                ''')
    st.code('''
            print("Somme des valeurs manquantes :",df.isna().sum().sum())
            Somme des valeurs manquantes : 354
            ''')
    st.markdown("Ce résultat représente 0,15% des données de notre modèle, nous supprimons ces données.")
                
    st.code('''
            df = df.dropna(axis = 0, how = 'any')
            print('Taille après dropna :', len(df))
            ''')
    st.markdown('''Il reste 230336 entrées post nettoyage. L’entraînement sur les différents modèles peut alors être réalisé.''')

  st.markdown("# :grey[Renommage des variables]")
  with st.expander("Vers plus de clarté"):
     st.code('''
             Colname_mapping = {'Tan': 'Type_approval_number',
                   'T': 'Type',
                   'Va': 'Variant',
                   'Mk': 'Make',
                   'Cn': 'Commercial_name',
                   'Ct': 'Category_vehicle_type_approved',
                   'm (kg)': 'Mass_kg',
                   'W (mm)': 'Wheel_Base_(length_mm)',
                   'At1 (mm)': 'Track_(width_mm)',
                   'Ft': 'Fuel_type',
                   'Fm': 'Fuel_mode',
                   'ec (cm3)': 'Engine_capacity_cm3',
                   'ep (KW)': 'Engine_power_KW',
                   'year': 'Reporting_year'}

                    df.rename(columns=Colname_mapping, inplace=True)

             ''')

elif page == pages[2]:
  st.header('3 - Modélisation', divider=True)

  st.markdown("# :grey[Méthodologie]")
  st.markdown("Nous cherchons à prédire des valeurs continues d'émissions de CO2 et nous allons donc utiliser des modèles de **régression**")
  st.markdown("Nous avons sélectionné les modèles suivants :")
  with st.expander("Random Forest Regressor"):
     st.image('streamlit_assets/Feature importance RandomForest.png', use_column_width=True)

  with st.expander("Linear Regressor"):
     st.image('streamlit_assets/Feature importance RegressionLineaire.png', use_column_width=True)

  with st.expander("Gradient Boosting Regressor"):
    st.image('streamlit_assets/Feature importance GradientBoost.png', use_column_width=True)
  
elif page == pages[3]:
  st.header('4 - Conclusion', divider=True)
  st.markdown("""
              Pour conclure notre étude sur les émission de CO2 des véhicules, plusieurs points clés émergent:
              - **Données limitées** : Nous avons exploité les données disponibles depuis 2015, mais leur recul est restreint.
              - **Surreprésentation des véhicules thermiques** : Notre jeu de données est largement composé de vehicules essence et diesel, ce qui reflète la forte présence de ces motorisation sur les routes.
              - **Variables influentes pour le rejet de CO2** : Le dimensionnement du véhicule (poids, taille de la cylindrée) et les spécifications du moteur se sont avérés plus significatifs pour prédire les émissions de CO2.
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
 

  import streamlit as st
  import pandas as pd
  import numpy as np
  import joblib
  from sklearn.ensemble import RandomForestRegressor
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler, RobustScaler
  from sklearn.metrics import f1_score

  # Chargement du dataset
  df = pd.read_csv('https://raw.githubusercontent.com/mogdan/Datascientest_CO2/refs/heads/main/streamlit_assets/Dataset_Rendu2_cleaned.csv', sep=',')

  # Séparation des colonnes numériques et catégorielles
  col_num = ['Mass_kg', 'Wheel_Base_(length_mm)', 'Track_(width_mm)', 'Engine_capacity_cm3', 'Engine_power_KW', 'Reporting_year']
  col_cat = ['Type_approval_number', 'Type', 'Variant', 'Make', 'Commercial_name', 'Category_vehicle_type_approved', 'Fuel_mode', 'Fuel_type']

  # Encodage fréquentiel des variables catégorielles
  def frequency_encoding(df, column):
    frequency = df[column].value_counts()
    df[column + '_encoded'] = df[column].map(frequency)
    return df

  for col in col_cat:
    df = frequency_encoding(df, col)

  # Supprimer les colonnes catégorielles d'origine
  df = df.drop(col_cat, axis=1)
  col_cat_encoded = [col + '_encoded' for col in col_cat]

  # Séparer les données en train/test
  X = df.drop('CO2_Emissions', axis=1)
  y = df['CO2_Emissions']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Appliquer le scaling
  scaler = RobustScaler()
  X_train[col_num] = scaler.fit_transform(X_train[col_num])
  # X_test[col_num] = scaler.transform(X_test[col_num])

  # Utiliser StandardScaler pour les variables encodées
  scaler_cat = StandardScaler()
  X_train[col_cat_encoded] = scaler_cat.fit_transform(X_train[col_cat_encoded])
  # X_test[col_cat_encoded] = scaler_cat.transform(X_test[col_cat_encoded])

  # # Entraîner le modèle RandomForest
  # model_rf = RandomForestRegressor()
  # model_rf.fit(X_train, y_train)
  # joblib.dump(model_rf, 'model_rf.joblib')

  # Chargement du modèle
  model_xgboost = joblib.load('model_XGBoost.joblib')

  # Interface utilisateur
  st.title("Application de calcul des émissions de CO2")
  st.header("Calculateur d'empreinte carbone pour les véhicules")

  # Entrées utilisateur
  col1, col2, col3 = st.columns(3)

  with col1:
    weekly_km = st.slider("📏 Distance moyenne hebdomadaire (en km)", 5, 1000, 200, 5)
    yearly_km = weekly_km * 52

  with col2:
    fuel_type = st.selectbox("⛽ Type de carburant", ["PETROL", "DIESEL", "LPG", "PETROL/ELECTRIC", "DIESEL/ELECTRIC", 'NG', 'E85', 'NG-BIOMETHANE'])

  with col3:
    engine_capacity = st.slider("🏎️ Cylindrée (en litres)", 0.5, 10.0, 1.6, 0.1)

  reporting_year = st.select_slider("📅 Année d'immatriculation du véhicule", range(2017, 2023), 2020)

  # Encodage du type de carburant
  fuel_type_freq = df['Fuel_type_encoded'].value_counts() / len(df)
  fuel_type_encoded = fuel_type_freq.get(fuel_type, 0)

  # Bouton de calcul
  if st.button("Calculer les émissions de CO2"):
    # Préparation des données pour la prédiction
    prediction_input = [reporting_year, engine_capacity, fuel_type_encoded]
    nombre_caracteristiques_attendues = len(X.columns)
    
    if len(prediction_input) < nombre_caracteristiques_attendues:
        prediction_input += [0] * (nombre_caracteristiques_attendues - len(prediction_input))

    prediction_input = np.array(prediction_input).reshape(1, -1)
    
    # Application les transformations pour normaliser les données d'entrée
    prediction_input[:, :len(col_num)] = scaler.transform(prediction_input[:, :len(col_num)])
    prediction_input[:, len(col_num):] = scaler_cat.transform(prediction_input[:, len(col_num):])

    # Prédiction
    CO2_emission = model_xgboost.predict(prediction_input)[0]
    yearly_emission = CO2_emission * yearly_km / 1000000
    yearly_emission = round(yearly_emission, 2)

    # Affichage des résultats
    st.header("Résultats")
    st.info(f"Émissions estimées pour {yearly_km} km par an : {yearly_emission} tonnes de CO2 par an")
    # st.warning("La limite maximale moyenne est de 282,963 tonnes de CO2 par habitant")
