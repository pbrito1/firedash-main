import streamlit as st
import os
import csv
import pandas as pd
import yfinance as yf
from datetime import datetime, date, timedelta

with open(os.getcwd()+'/dashboard/pages/ifix.csv', newline='') as f:
    reader = csv.reader(f)
    fundos = [i[0] + '.SA' for i in list(reader)]

principais = ['DEVA11.SA', 'MFII11.SA', 'MXRF11.SA', 'XPSF11.SA', 'RBFF11.SA']

def get_metric(ticker):
    df = pd.DataFrame(yf.download(ticker, datetime.today() - timedelta(5),datetime.today()))
    delta = str(round((df.iloc[-1].Close - df.iloc[-2].Close) / df.iloc[-2].Close * 100, 2)) + '%'
    close = round(float(df.iloc[-1].Close),2)
    st.metric(ticker,close,delta)
    

with st.sidebar:
    st.subheader('Comparar Ações')
    input_ac1 = st.selectbox('Fundo 1', fundos, index=fundos.index(principais[0]))
    input_ac2 = st.selectbox('Fundo 2', fundos, index=fundos.index(principais[1]))
    input_ac3 = st.selectbox('Fundo 3', fundos, index=fundos.index(principais[2]))
    input_ac4 = st.selectbox('Fundo 4', fundos, index=fundos.index(principais[3]))
    input_ac5 = st.selectbox('Fundo 5', fundos, index=fundos.index(principais[4]))
    dt_inicio =st.date_input('Data Inicial', key='1', value=date(2024,1,1))
    dt_fim_br = st.date_input('Data Final',key='2')


st.title('Fundos Imobliários')
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

st.subheader('Comparar FIIs')
chart_data = pd.DataFrame(yf.download([input_ac1,input_ac2,input_ac3,input_ac4,input_ac5], dt_inicio,dt_fim_br)['Adj Close'])
st.line_chart(chart_data)
