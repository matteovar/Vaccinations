import streamlit as st
import pandas as pd
from src.main import df_final
from src.utils.functions import fake_news_charts

st.set_page_config(layout="wide")

st.title("📉 Análise Enganosa (Fake News)")
st.markdown("Nesta seção estão exemplos de como gráficos podem ser manipulados para induzir interpretações incorretas.")

if df_final is not None:
    fake_news_charts(df_final)
