import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, date, timedelta

df_html = pd.read_html('https://finance.yahoo.com/world-indices/')
df = pd.DataFrame(data=df_html[0])
indices = df[['Symbol', 'Name']]

principais = ['^BVSP', '^GSPC', '^N100', '^N225', '000001.SS']

def get_metric(name):
    ticker = indices.iloc[indices.index[indices['Name'] == name].tolist()[0]].Symbol
    df = pd.DataFrame(yf.download(ticker, datetime.today() - timedelta(5),datetime.today()))
    delta = str(round((df.iloc[-1].Close - df.iloc[-2].Close) / df.iloc[-2].Close * 100, 2)) + '%'
    close = str(round(float(df.iloc[-1].Close) / 1000,2)) + 'K'
    st.metric(ticker,close,delta)

def get_id_indice(label):
    return indices.index[indices['Symbol'] == label].tolist()[0]

with st.sidebar:
    st.subheader('Comparar Índices')
    input_ac1 = st.selectbox('Índice 1', indices.Name, index=get_id_indice(principais[0]))
    input_ac2 = st.selectbox('Índice 2', indices.Name, index=get_id_indice(principais[1]))
    input_ac3 = st.selectbox('Índice 3', indices.Name, index=get_id_indice(principais[2]))
    input_ac4 = st.selectbox('Índice 4', indices.Name, index=get_id_indice(principais[3]))
    input_ac5 = st.selectbox('Índice 5', indices.Name, index=get_id_indice(principais[4]))
    dt_inicio =st.date_input('Data Inicial', key='1', value=date(2024,1,1))
    dt_fim_br = st.date_input('Data Final',key='2')


st.title('Índices Mundiais')
st.subheader('Valor Atual')

col10, col20, col30, col40, col50 = st.columns(5)

with col10:
    get_metric(input_ac1)
with col20:
    get_metric(input_ac2)
with col30:
    get_metric(input_ac3)
with col40:
    get_metric(input_ac4)
with col50:
    get_metric(input_ac5)

st.markdown('---')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    get_metric(indices.Name[1])
    st.markdown('---')
    get_metric(indices.Name[2])
    st.markdown('---')
    get_metric(indices.Name[12])

with col2:
    get_metric(indices.Name[15])
    st.markdown('---')
    get_metric(indices.Name[16])
    st.markdown('---')
    get_metric(indices.Name[24])

with col3:
    get_metric(indices.Name[20])
    st.markdown('---')
    get_metric(indices.Name[17])
    st.markdown('---')
    get_metric(indices.Name[18])

with col4:
    get_metric(indices.Name[4])
    st.markdown('---')
    get_metric(indices.Name[8])
    st.markdown('---')
    get_metric(indices.Name[10])

with col5:
    get_metric(indices.Name[19])
    st.markdown('---')
    get_metric(indices.Name[32])
    st.markdown('---')
    get_metric(indices.Name[0])

