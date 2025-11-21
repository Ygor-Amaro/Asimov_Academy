import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

data_list = [
    "data/CLEAN_FIFA17_official_data.csv",
    "data/CLEAN_FIFA18_official_data.csv",
    "data/CLEAN_FIFA19_official_data.csv",
    "data/CLEAN_FIFA20_official_data.csv",
    "data/CLEAN_FIFA21_official_data.csv",
    "data/CLEAN_FIFA22_official_data.csv",
    "data/CLEAN_FIFA23_official_data.csv",
]

if "data" not in st.session_state:
    dfs = []  # Lista temporária para armazenar os DataFrames
    for csv_file in data_list:
        df = pd.read_csv(csv_file)
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)  # Concatena todos os DataFrames
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    df = df[df["Value(£)"] > 0]
    df = df.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = combined_df

st.markdown("# FIFA23 OFFICIAL DATASET ⚽️")
st.sidebar.markdown("Desenvolvido por [Ygor Amaro](https://github.com/Ygor-Amaro) e [Asimov Academy](https://asimov.academy/)⚽️")

btn = st.button("Acesse os dados do Kaggle 🚀",)
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data?resource=download")