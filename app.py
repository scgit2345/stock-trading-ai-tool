import streamlit as st

# Basic debugging
st.write("App is running...")

# Title
st.title("Stock Trading AI Tool")

# Input field for stock ticker
ticker = st.text_input("Enter a stock ticker:", "AAPL")

# Button to analyze stock
if st.button("Analyze Stock"):
    st.write(f"Fetching data and analyzing {ticker}...")
    st.write(f"AI Prediction for {ticker}: 🚀 Bullish (Sample Output)")