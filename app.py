import streamlit as st
import traceback

st.title("Stock Trading AI Tool")

try:
    # Input field for stock ticker
    ticker = st.text_input("Enter a stock ticker:", "AAPL")

    # Simulating AI analysis
    st.write(f"Fetching data and analyzing {ticker}...")

    # Button to analyze stock
    if st.button("Analyze Stock"):
        st.write(f"AI Prediction for {ticker}: 🚀 Bullish (Sample Output)")

except Exception as e:
    error_message = traceback.format_exc()
    st.error(f"An error occurred: {e}")
    st.text_area("Detailed Error Log:", error_message, height=200)