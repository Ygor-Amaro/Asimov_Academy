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
    dfs = []
    for csv_file in data_list:
        df = pd.read_csv(csv_file)
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True) 

    combined_df = combined_df[combined_df["Contract Valid Until"] >= datetime.today().year]
    combined_df = combined_df[combined_df["Value(£)"] > 0]
    combined_df = combined_df.sort_values(by="Overall", ascending=False)

    st.session_state["data"] = combined_df

st.markdown("# FIFA23 OFFICIAL DATASET ⚽️")
st.sidebar.markdown("Desenvolvido por [Ygor Amaro](https://github.com/Ygor-Amaro) e [Asimov Academy](https://asimov.academy/)⚽️")

btn = st.button("Acesse os dados do Kaggle 🚀",)
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data?resource=download")

st.markdown("""
Sobre o Conjunto de Dados
CONTEXTO

O Conjunto de Dados de Jogadores de Futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. 
O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes contratuais e afiliações a clubes. 
Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, 
permitindo estudar atributos dos jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.

COLUNAS

    1. ID: Um identificador único para cada jogador.
    2. Name: O nome do jogador.
    3. Age: A idade do jogador no momento da coleta dos dados.
    4. Photo: Um link ou referência para a fotografia do jogador.
    5. Nationality: A nacionalidade do jogador.
    6. Flag: A bandeira nacional associada à nacionalidade do jogador.
    7. Overall: A classificação geral das habilidades e capacidades do jogador.
    8. Potential: A classificação potencial que representa o desenvolvimento futuro do jogador.
    9. Club: A afiliação atual do jogador ao clube.
    10. Club Logo: Um link ou referência ao logotipo do clube do jogador.
    11. Value (£): O valor de mercado estimado do jogador em libras (£).
    12. Wage (£): O salário semanal do jogador em libras (£).
    13. Special: Um valor numérico que representa as habilidades especiais do jogador.
    14. Preferred Foot: O pé preferido do jogador para jogar.
    15. International Reputation: Uma classificação que indica a reputação internacional do jogador.
    16. Weak Foot: Uma classificação que representa as habilidades do pé mais fraco do jogador.
    17. Skill Moves: O número de movimentos de habilidade que o jogador possui.
    18. Work Rate: A taxa de trabalho do jogador.
    19. Body Type: A constituição física ou tipo corporal do jogador.
    20. Real Face: Indica se o jogador tem uma representação facial real.
    21. Position: A posição preferida do jogador em campo.
    22. Joined: A data em que o jogador ingressou no clube atual.
    23. Loaned From: O clube do qual o jogador está atualmente emprestado.
    24. Contract Valid Until: A data até a qual o contrato do jogador é válido.
    25. Height (cm.): A altura do jogador em centímetros.
    26. Weight (lbs.): O peso do jogador em libras.
    27. Release Clause (£): O valor da cláusula de rescisão do jogador em libras (£).
    28. Kit Number: O número da camisa do jogador.
    29. Best Overall Rating: A maior classificação geral do jogador.
    30. Year Joined: O ano em que o jogador ingressou no clube atual.
""")