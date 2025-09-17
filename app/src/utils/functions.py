import pandas as pd
import plotly.express as px
import streamlit as st
from src.utils.plotly_charts.line_chart import line
from src.utils.plotly_charts.bar_chart import bar
from src.utils.plotly_charts.subplot_chart import subplot_dual_axis
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
# =====================
#   FAKE NEWS CHARTS
# =====================


def fake_news_charts(df_final: pd.DataFrame):

    # === Narrativa 1 ===
    st.subheader('Narrativa 1: A Anomalia nos Óbitos Durante a Vacinação')
    df_narrativa1 = df_final[(df_final['data'] >= '2021-01-01')
                             & (df_final['data'] <= '2021-07-31')]
    fig1_invertido = make_subplots(specs=[[{"secondary_y": True}]])
    fig1_invertido.add_trace(go.Scatter(x=df_narrativa1['data'], y=df_narrativa1['obitosNovos_mm7'],
                             name='Anomalia de Óbitos Diários', line=dict(color='yellow', width=3)), secondary_y=False)
    fig1_invertido.add_trace(go.Bar(x=df_narrativa1['data'], y=df_narrativa1['vacinacoes_acumuladas'],
                             name='Total de Doses Aplicadas', marker_color='grey', opacity=0.5), secondary_y=True)
    fig1_invertido.update_layout(
        title_text='Óbitos (Eixo Invertido) vs. Vacinas Acumuladas', template='plotly_dark')
    fig1_invertido.update_yaxes(title_text="<b>Óbitos Diários (Eixo Invertido)</b>",
                                secondary_y=False, color='yellow', autorange="reversed")
    fig1_invertido.update_yaxes(title_text="<b>Total de Doses Aplicadas</b>", secondary_y=True, color='grey') 
    st.plotly_chart(fig1_invertido, use_container_width=True) 
    st.markdown("---")

    # === Narrativa 2 ===
    st.subheader("Narrativa 2: Recorde de Casos com Vasta Cobertura Vacinal")
    df_narrativa2 = df_final[(df_final["data"] >= "2021-08-01")
                             & (df_final["data"] <= "2022-05-31")]

    subplot_dual_axis(
        x=df_narrativa2["data"],
        y1=df_narrativa2["casosNovos_mm7"],
        y2=df_narrativa2["vacinacoes_acumuladas"],
        name1="Média de Casos Diários",
        name2="Total de Doses Aplicadas",
        color1="orange",
        color2="lightgreen",
        title="Casos Diários vs. Vacinas Acumuladas (Onda Ômicron)",
        y1_title="Média de Casos Diários",
        y2_title="Total de Doses Aplicadas",
    )

    st.markdown("---")

    # === Narrativa 3 ===
    st.subheader(
        "Narrativa 3: Novas Variantes Surgem Conforme a Vacinação Avança")
    fig = px.line(
        df_final,
        x="data",
        y="vacinacoes_acumuladas",
        title="Avanço da Vacinação e o Surgimento de Novas Variantes",
        template="plotly_dark",
    )
    fig.update_traces(line_color="lightgreen", line_width=3)

    # Linhas verticais das variantes
    variantes = {
        "2021-03-01": ("Dominância da Variante GAMA", "yellow", 0.8),
        "2021-09-01": ("Dominância da Variante DELTA", "orange", 0.6),
        "2022-01-15": ("Dominância da Variante ÔMICRON", "red", 0.9),
    }

    for date, (label, color, pos) in variantes.items():
        fig.add_vline(x=pd.to_datetime(date), line_width=2,
                      line_dash="dash", line_color=color)
        fig.add_annotation(
            x=pd.to_datetime(date),
            y=df_final["vacinacoes_acumuladas"].max() * pos,
            text=label,
            showarrow=False,
            yshift=10,
            font=dict(color=color),
        )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

    # === Narrativa 4 ===
    st.subheader(
        "Narrativa 4: Correlação Inquieta entre Doses Diárias e Óbitos")
    st.markdown("""
    Ao analisar os dados diários, sem médias móveis, observamos um padrão inquietante:
    picos de óbitos que parecem ocorrer logo após dias de vacinação em massa.
    """)

    df_narrativa3 = df_final[(df_final["data"] >= "2021-06-15")
                             & (df_final["data"] <= "2021-07-15")]

    subplot_dual_axis(
        x=df_narrativa3["data"],
        y1=df_narrativa3["vacinacoes"],
        y2=df_narrativa3["obitosNovos"],
        name1="Doses Diárias Aplicadas",
        name2="Óbitos Diários Registrados",
        color1="royalblue",
        color2="red",
        title="Doses Diárias vs. Óbitos Diários (Jun-Jul 2021)",
        y1_title="Doses Diárias",
        y2_title="Óbitos Diários",
        bar=True,
    )

    st.markdown("---")

    # === Narrativa 5 ===
    st.subheader('Narrativa 5: A Maioria das Mortes Ocorreu na "Era Vacinal"')
    data_inicio_vacinacao = pd.to_datetime("2021-01-17")
    obitos_antes = df_final[df_final["data"] <
                            data_inicio_vacinacao]["obitosNovos"].sum()
    obitos_depois = df_final[df_final["data"] >=
                             data_inicio_vacinacao]["obitosNovos"].sum()

    dados_comparativos = pd.DataFrame({
        "Período": ["Antes da Vacinação", "Durante/Após a Vacinação"],
        "Total de Óbitos": [obitos_antes, obitos_depois],
    })

    bar(
        dados_comparativos,
        x="Período",
        y="Total de Óbitos",
        title="Comparativo de Óbitos Totais: Pré e Pós-Vacinação",
        color="Período",
    )


# =====================
#   REAL CHARTS
# =====================
def real_charts(df_final: pd.DataFrame):

    # === Gráfico 1 ===
    st.subheader("Gráfico 1: A Prova Definitiva - Queda da Taxa de Letalidade")
    subplot_dual_axis(
        x=df_final["data"],
        y1=df_final["taxa_letalidade_mm14"],
        y2=df_final["doses_por_100_hab"],
        name1="Taxa de Letalidade (Média 14d) %",
        name2="Doses por 100 Habitantes",
        color1="deepskyblue",
        color2="lightgreen",
        title="Taxa de Letalidade da COVID-19 vs. Avanço da Vacinação",
        y1_title="Taxa de Letalidade (%)",
        y2_title="Doses por 100 Habitantes",
    )

    st.markdown("---")

    # === Gráfico 2 ===
    st.subheader("Gráfico 2: O 'Descolamento' das Curvas de Casos e Óbitos")
    df_plot = df_final.dropna(
        subset=["casosNovos_mm14", "obitosNovos_mm14"]).copy()
    df_plot["casos_normalizados"] = (
        df_plot["casosNovos_mm14"] / df_plot["casosNovos_mm14"].max()) * 100
    df_plot["obitos_normalizados"] = (
        df_plot["obitosNovos_mm14"] / df_plot["obitosNovos_mm14"].max()) * 100

    line(
        df=df_plot,
        x="data",
        y=["casos_normalizados", "obitos_normalizados"],
        title="Comparativo Normalizado de Casos e Óbitos",
        x_title="Data",
        y_title="Percentual em Relação ao Pico Histórico (%)",
    )
