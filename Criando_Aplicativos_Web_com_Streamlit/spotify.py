#Criando Aplicativos Web com Streamlit

import pandas as pd
import streamlit as st

df = pd.read_csv(
    r'C:/Users/ykba0/OneDrive/Documentos/ASIMOV_ACADEMY/Criando_Aplicativos_Web_com_Streamlit/DataSpotify.csv', 
    engine='python',
    encoding='utf-8',
    sep=','
)

print(df.columns)
df[df["Stream"] > 1000000000] #Filtra as músicas com mais de 1 bilhão de streams