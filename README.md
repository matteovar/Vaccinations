# Análise Crítica de Dados da COVID-19: Fake News vs. Realidade
## 1. Objetivo do Projeto
  Este projeto é um estudo de caso acadêmico que demonstra como a visualização de dados pode ser uma ferramenta poderosa tanto para a informação quanto para a desinformação. Utilizando um conjunto de dados públicos sobre a pandemia de COVID-19 e a vacinação no Brasil, esta aplicação interativa constrói duas narrativas opostas:
  
  Uma narrativa enganosa (Fake News): Que utiliza técnicas de manipulação visual e omissão de contexto para gerar dúvidas sobre a eficácia das vacinas.
  
  Uma narrativa factual (A Realidade): Que aplica métricas estatísticas corretas para revelar o impacto real e positivo da campanha de vacinação na redução de desfechos graves da doença.
  
  O objetivo final é educacional: destacar a importância do pensamento crítico e da literacia de dados na interpretação de gráficos e relatórios.

## 2. Funcionalidades
### A aplicação, construída com Streamlit, oferece:

  Interface Interativa: Um painel web de fácil navegação.
  
  Comparação Direta: Duas abas principais que separam claramente a "Análise Enganosa" da "Análise Correta".
  
  Visualizações Múltiplas: Diversos gráficos para cada narrativa, explorando diferentes facetas dos dados.
  
  Textos Explicativos: Cada gráfico é acompanhado de uma explicação que guia o usuário através da narrativa proposta, seja ela enganosa ou factual.

## 3. Conceitos e Técnicas Demonstradas
### Na Aba "Análise Enganosa (Fake News)":
  Cherry-Picking: Seleção deliberada de intervalos de tempo que apoiam uma conclusão pré-determinada.
  
  Falsa Causalidade: Insinuação de que correlação implica causalidade (ex: vacinação avança, novas variantes surgem).
  
  Métricas Enganosas: Foco em números absolutos (total de óbitos) em vez de taxas proporcionais.
  
  Manipulação Visual: Inversão de eixos para distorcer completamente a percepção de um gráfico.

### Na Aba "Análise Correta (A Realidade)":
  Uso de Taxa de Letalidade (CFR): Demonstração de como a proporção de mortes por caso despencou com a vacinação.
  
  "Descolamento" das Curvas: Análise visual que mostra como a vacinação quebrou a ligação entre o número de casos e o número de óbitos.
  
  Importância do Contexto: A explicação leva em conta fatores cruciais omitidos na outra análise, como o surgimento de novas variantes (Gama, Ômicron).

## 4. Fontes de Dados
  Dados de Casos e Óbitos: Painel COVID-19 Brasil, disponibilizado pelo Ministério da Saúde. Os arquivos (HIST_PAINEL_COVIDBR_*.csv) são recortes temporais destes dados.
  
  Dados de Vacinação: Arquivo vaccination.csv, compilado com dados diários da campanha de vacinação.

## 5. Tecnologias Utilizadas
  Linguagem: Python 3.9+
  
  Bibliotecas Principais:
  
  Pandas: Para manipulação e processamento dos dados.
  
  Streamlit: Para a criação da aplicação web interativa.
  
  Plotly Express & Graph Objects: Para a geração dos gráficos interativos.

## 6. Como Executar o Projeto Localmente
  Siga os passos abaixo para rodar a aplicação em sua máquina.
  
  Pré-requisitos
  Git instalado.
  
  Python 3.9 ou superior instalado.

# Passos
Clone o repositório:

```git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
*Crie e ative um ambiente virtual (recomendado):*
Para Windows
```
python -m venv venv
.\venv\Scripts\activate
```
Para macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```
Em seguida, instale-o:
```
pip install -r requirements.txt
```
Execute a aplicação Streamlit:
```
streamlit run seu_script_principal.py
```
