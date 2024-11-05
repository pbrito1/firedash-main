import streamlit as st
import pandas as pd
import yfinance as yf
import investpy as inv
from datetime import datetime, date, timedelta

df_html = pd.read_html('https://economia.uol.com.br/cotacoes/bolsas/')
altas = pd.DataFrame(data=df_html[1])
baixas = pd.DataFrame(data=df_html[2])
negociadas =pd.DataFrame(data=df_html[3])

def get_metric(metric, indice):
    ticker = metric.iloc[indice, 0]
    close = metric.iloc[indice, 2]
    delta = metric.iloc[indice, 1]
    st.metric(ticker, close, delta)

st.title('Ações em Destaques',anchor=False)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Altas',anchor=False)
    get_metric(altas, 0)
    get_metric(altas, 1)
    get_metric(altas, 2)
    get_metric(altas, 3)
    get_metric(altas, 4)

with col2:
    st.subheader('Baixas',anchor=False)
    get_metric(baixas, 0)
    get_metric(baixas, 1)
    get_metric(baixas, 2)
    get_metric(baixas, 3)
    get_metric(baixas, 4)
    
with col3:
    st.subheader('Mais Negociadas',anchor=False)
    get_metric(negociadas, 0)
    get_metric(negociadas, 1)
    get_metric(negociadas, 2)
    get_metric(negociadas, 3)
    get_metric(negociadas, 4)