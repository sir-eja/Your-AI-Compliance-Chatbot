import streamlit as st
import pandas as pd

st.title("Chatbot Performance Dashboard")

# Sample Data
data = pd.DataFrame({
    "User Query": ["Where is my order?", "What are your working hours?"],
    "Bot Response": ["Your order has been shipped.", "We are open 9 AM - 5 PM."]
})

st.dataframe(data)
