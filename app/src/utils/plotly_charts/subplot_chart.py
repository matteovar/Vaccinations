import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def subplot_dual_axis(
    x,
    y1,
    y2,
    name1: str,
    name2: str,
    color1: str,
    color2: str,
    title: str,
    y1_title: str,
    y2_title: str,
    bar: bool = False,
    reversed_y: bool = False,
):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    if bar:
        fig.add_trace(go.Bar(x=x, y=y1, name=name1, marker_color=color1), secondary_y=False)
    else:
        fig.add_trace(go.Scatter(x=x, y=y1, name=name1, line=dict(color=color1, width=3)), secondary_y=False)

    fig.add_trace(go.Scatter(x=x, y=y2, name=name2, line=dict(color=color2, width=2, dash="dot")), secondary_y=True)

    fig.update_layout(title_text=title, template="plotly_dark")
    fig.update_yaxes(title_text=y1_title, secondary_y=False, color=color1, autorange="reversed" if reversed_y else True)
    fig.update_yaxes(title_text=y2_title, secondary_y=True, color=color2)

    st.plotly_chart(fig, use_container_width=True)
