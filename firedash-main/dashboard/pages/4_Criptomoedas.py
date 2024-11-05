import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, date, timedelta

df_html = pd.read_html('https://finance.yahoo.com/crypto')
df = pd.DataFrame(data=df_html[0])
criptos = df[['Symbol', 'Name']]

principais = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD', 'DOGE-USD']

def get_metric(name):
    ticker = criptos.iloc[criptos.index[criptos['Name'] == name].tolist()[0]].Symbol
    df = pd.DataFrame(yf.download(ticker, datetime.today() - timedelta(5),datetime.today()))
    delta = str(round((df.iloc[-1].Close - df.iloc[-2].Close) / df.iloc[-2].Close * 100, 2)) + '%'
    close = round(float(df.iloc[-1].Close),2)
    st.metric(ticker,close,delta)
    
def get_id_indice(label):
    return criptos.index[criptos['Symbol'] == label].tolist()[0]

def get_ticker(name):
    return criptos.iloc[criptos.index[criptos['Name'] == name].tolist()[0]].Symbol

with st.sidebar:
    st.subheader('Comparar Ações')
    input_ac1 = st.selectbox('Índice 1', criptos.Name, index=get_id_indice(principais[0]))
    input_ac2 = st.selectbox('Índice 2', criptos.Name, index=get_id_indice(principais[1]))
    input_ac3 = st.selectbox('Índice 3', criptos.Name, index=get_id_indice(principais[2]))
    input_ac4 = st.selectbox('Índice 4', criptos.Name, index=get_id_indice(principais[3]))
    input_ac5 = st.selectbox('Índice 5', criptos.Name, index=get_id_indice(principais[4]))
    dt_inicio =st.date_input('Data Inicial', key='1', value=date(2024,1,1))
    dt_fim_br = st.date_input('Data Final',key='2')


st.title('Criptomoedas')
st.subheader('Valor Atual')
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    get_metric(input_ac1)

with col2:
    get_metric(input_ac2)

with col3:
    get_metric(input_ac3)

with col4:
    get_metric(input_ac4)

with col5:
    get_metric(input_ac5)

st.subheader('Comparar Cripto')
chart_data = pd.DataFrame(yf.download([get_ticker(input_ac1),get_ticker(input_ac2),get_ticker(input_ac3),get_ticker(input_ac4),get_ticker(input_ac5)], dt_inicio,dt_fim_br)['Adj Close'])
st.line_chart(chart_data)