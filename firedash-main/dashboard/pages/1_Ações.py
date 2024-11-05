import streamlit as st
import pandas as pd
import investpy as inv
import yfinance as yf
from datetime import datetime, date, timedelta

tickers_br = [item + '.SA' for item in inv.get_stocks_list('brazil')]
tickers_us = inv.get_stocks_list('United States')
tickers_us.append('META')

principais_br = ['PETR3.SA','MGLU3.SA','VALE3.SA','ITSA4.SA','ABEV3.SA']
principais_us = ['MSFT','NFLX','NVDA','COKE','META']

def get_metric(ticker):
    df = pd.DataFrame(yf.download(ticker, datetime.today() - timedelta(5),datetime.today()))
    delta = str(round((df.iloc[-1].Close - df.iloc[-2].Close) / df.iloc[-2].Close * 100, 2)) + '%'
    close = round(float(df.iloc[-1].Close),2)
    st.metric(ticker,close,delta)


with st.sidebar:
    st.subheader('Selecione um Mercado')
    local = st.selectbox('', ['Brasil', 'Estados Unidos'])

if local == 'Brasil':
    st.title('Ações Brasileiras', anchor=False)
    st.subheader('Valor Atual', anchor=False)

    with st.sidebar:
        st.subheader('Comparar Ações')
        input_ac1_br = st.selectbox('Ação 1', tickers_br, index=tickers_br.index(principais_br[0]))
        input_ac2_br = st.selectbox('Ação 2', tickers_br, index=tickers_br.index(principais_br[1]))
        input_ac3_br = st.selectbox('Ação 3', tickers_br, index=tickers_br.index(principais_br[2]))
        input_ac4_br = st.selectbox('Ação 4', tickers_br, index=tickers_br.index(principais_br[3]))
        input_ac5_br = st.selectbox('Ação 5', tickers_br, index=tickers_br.index(principais_br[4]))
        dt_inicio_br =st.date_input('Data Inicial', key='1', value=date(2024,1,1))
        dt_fim_br = st.date_input('Data Final',key='2')



    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        get_metric(input_ac1_br)

    with col2:
        get_metric(input_ac2_br)

    with col3:
        get_metric(input_ac3_br)

    with col4:
        get_metric(input_ac4_br)

    with col5:
        get_metric(input_ac5_br)


    st.subheader('Comparar Ações')
    chart_data = pd.DataFrame(yf.download([input_ac1_br,input_ac2_br,input_ac3_br,input_ac4_br,input_ac5_br], dt_inicio_br,dt_fim_br)['Adj Close'])
    st.line_chart(chart_data)

else:
    st.title('Ações Americanas (S&P 500)', anchor=False)
    st.subheader('Valor Atual', anchor=False)

    with st.sidebar:
        st.subheader('Comparar Ações')
        input_ac1_us = st.selectbox('Ação 1', tickers_us, index=tickers_us.index(principais_us[0]))
        input_ac2_us = st.selectbox('Ação 2', tickers_us, index=tickers_us.index(principais_us[1]))
        input_ac3_us = st.selectbox('Ação 3', tickers_us, index=tickers_us.index(principais_us[2]))
        input_ac4_us = st.selectbox('Ação 4', tickers_us, index=tickers_us.index(principais_us[3]))
        input_ac5_us = st.selectbox('Ação 5', tickers_us, index=tickers_us.index(principais_us[4]))
        dt_inicio_us =st.date_input('Data Inicial',key='3', value=date(2024,1,1))
        dt_fim_us = st.date_input('Data Final', key='4')




    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        get_metric(input_ac1_us)

    with col2:
        get_metric(input_ac2_us)

    with col3:
        get_metric(input_ac3_us)

    with col4:
        get_metric(input_ac4_us)

    with col5:
        get_metric(input_ac5_us)


    st.subheader('Comparar Ações')
    chart_data = pd.DataFrame(yf.download([input_ac1_us,input_ac2_us,input_ac3_us,input_ac4_us,input_ac5_us], dt_inicio_us,dt_fim_us)['Adj Close'])
    st.line_chart(chart_data)