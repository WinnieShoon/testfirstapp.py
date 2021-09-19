
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **Closing Price** and **Volume** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'

# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")

st.write("""
## Volume Price
""")

