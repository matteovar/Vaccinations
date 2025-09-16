import pandas as pd
import streamlit as st

st.set_page_config(page_title="COVID-19", layout="wide")


def main():

    pages_1 = {
        "Pages": [
            st.Page("src/pages/Vision_on_Pandemic.py", title="Pandemic Overview"),
        ],
    }

    pg = st.navigation(pages_1)
    pg.run()


if __name__ == "__main__":
    main()
