import streamlit as st
import pandas as pd
from src.main import df_final
from src.utils.functions import real_charts

st.set_page_config(layout="wide")

st.title("📈 Análise Correta (A Realidade)")
st.success("Aqui apresentamos os gráficos com métricas adequadas, que revelam o impacto real da vacinação.")

if df_final is not None:
    real_charts(df_final)
