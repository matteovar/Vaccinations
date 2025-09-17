import streamlit as st

# Esta estrutura usa a nova funcionalidade st.Page, que é ótima.
# Apenas garanta que a versão do seu Streamlit seja compatível (1.23.0 ou superior).
def main():
    pages_1 = {
        "Pages": [
            st.Page("src/pages/analise_fake.py", title="Fake Storytelling"),
            st.Page("src/pages/analise_real.py", title="True Storytelling"),
        ],
    }

    pg = st.navigation(pages_1)
    st.set_page_config(page_title="COVID-19 Storytelling", layout="wide")
    pg.run()


if __name__ == "__main__":
    main()