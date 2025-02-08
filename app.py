import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Stock Market Analysis')

ticker_symbol = st.text_input('Enter Stock Symbol (e.g., AAPL):', 'AAPL')

if ticker_symbol:
    stock_data = yf.Ticker(ticker_symbol)
    df = stock_data.history(period='1y')

    st.line_chart(df.Close)

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

pg = st.navigation(
    {
        "Reports": [dashboard],
        "Tools": [search, history],
    }
)

pg.run()