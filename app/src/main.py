import pandas as pd
import streamlit as st


df1 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2020_Parte1_05set2025.csv', sep=';')
df2 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2020_Parte2_05set2025.csv', sep=';')
df3 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2021_Parte1_05set2025.csv', sep=';')
df4 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2021_Parte2_05set2025.csv', sep=';')
df5 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2022_Parte1_05set2025.csv', sep=';')
df6 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2022_Parte2_05set2025.csv', sep=';')
df7 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2023_Parte1_05set2025.csv', sep=';')
df8 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2023_Parte2_05set2025.csv', sep=';')
df9 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2024_Parte1_05set2025.csv', sep=';')
df10 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2024_Parte2_05set2025.csv', sep=';')
df11 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2025_Parte1_05set2025.csv', sep=';')
df12 = pd.read_csv(
    'app/data/input/HIST_PAINEL_COVIDBR_2025_Parte2_05set2025.csv', sep=';')
df13 = pd.read_csv('app/data/input/vaccination.csv', sep=',')

df_cont = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8,
                    df9, df10, df11, df12], ignore_index=True)

df_cont["data"] = pd.to_datetime(df_cont["data"])
df_cont = df_cont[df_cont["regiao"] == "Brasil"]

df13["regiao"] = "Brasil"
df13["data"] = pd.to_datetime(df13["data"])
df13['vacinacoes'] = df13['vacinacoes'].astype(
    str).str.replace(',', '').astype(float)

df_final = pd.merge(
    df_cont,
    df13,
    on=["data", "regiao"],   # colunas em comum
    how="left"               # mantém todas as linhas de df_cont, adicionando as colunas de df13
)

df_final['vacinacoes'] = df_final['vacinacoes'].fillna(0)

df_final = df_final.sort_values(by="data")

populacao_brasil = df_final['populacaoTCU2019'].dropna().iloc[0]
        

df_final['vacinacoes_acumuladas'] = df_final['vacinacoes'].cumsum()
df_final['doses_por_100_hab'] = (df_final['vacinacoes_acumuladas'] / populacao_brasil) * 100

df_final['casosNovos_mm7'] = df_final['casosNovos'].rolling(window=7).mean()
df_final['obitosNovos_mm7'] = df_final['obitosNovos'].rolling(window=7).mean()
df_final['casosNovos_mm14'] = df_final['casosNovos'].rolling(window=14).mean()
df_final['obitosNovos_mm14'] = df_final['obitosNovos'].rolling(
    window=14).mean()

soma_obitos_14d = df_final['obitosNovos'].rolling(window=14).sum()
soma_casos_14d = df_final['casosNovos'].rolling(window=14).sum()
df_final['taxa_letalidade_mm14'] = (soma_obitos_14d / soma_casos_14d) * 100

df_final = df_final.dropna(subset=['casosNovos_mm7', 'obitosNovos_mm7'])
