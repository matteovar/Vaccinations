import pandas as pd
import plotly.express as px
import streamlit as st

def bar(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    color: str = None,
    orientation: str = "v",
    text_auto: bool = True,
):
    bar_view = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        orientation=orientation,
        text_auto=True if text_auto else None,
        title=title,
    )

    st.plotly_chart(bar_view, use_container_width=True)
