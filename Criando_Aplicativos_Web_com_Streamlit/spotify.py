#Criando Aplicativos Web com Streamlit

import pandas as pd
import streamlit as st

df = pd.read_csv('Criando_Aplicativos_Web_com_Streamlit\01 Spotify.csv')
df[df["Streams"] > 1000000000] #Filtra as músicas com mais de 1 bilhão de streams