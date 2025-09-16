import pandas as pd
import streamlit as st
from src.main import (
    vaccination,
)
from src.utils.cards import create_cards
from src.utils.plotly_charts.line_chart import line


def display_title():
    st.markdown(
        """
        <h1 style='text-align: center; font-family: Arial, sans-serif;'>
            Pandemic Overview 
        </h1>
        <h2 style="color: #0638a1; text-align: center;">
            From December 2020 to May 2021
        </h2>
        """,
        unsafe_allow_html=True,
    )


def show_total_vaccinations_per_day():
    total_vaccinations = (
        vaccination.groupby("date")["total_vaccinations"].sum().reset_index()
    )
    line(
        df=total_vaccinations,
        x="date",
        y="total_vaccinations",
        title="Total Vaccinations per Day",
        x_title="Date",
    )


def show_main():
    display_title()
    show_total_vaccinations_per_day()


show_main()
