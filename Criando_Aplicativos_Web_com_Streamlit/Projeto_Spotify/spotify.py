#Criando Aplicativos Web com Streamlit

import pandas as pd
import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Spotify Songs",
)

df = pd.read_csv(
    r'C:/Users/ykba0/OneDrive/Documentos/ASIMOV_ACADEMY/Criando_Aplicativos_Web_com_Streamlit/DataSpotify.csv', 
    engine='python',
    encoding='utf-8',
    sep=','
)
print(df.columns)
df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]

albuns = df_filtered["Album"].value_counts().index
album = st.sidebar.selectbox("Album", albuns)
df_filtered2 = df[df["Album"] == album]

col1, col2 = st.columns(2)

col1.bar_chart(df_filtered2["Stream"])
col2.bar_chart(df_filtered2["most_playedon"])
st.write(artist)