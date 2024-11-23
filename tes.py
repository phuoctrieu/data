import requests
import streamlit as st
import json

# Load API keys from config file
with open('config.json', 'r') as f:
    config = json.load(f)

api_key = config["api_key"]
api_secret = config["api_secret"]

# Set headers for the request (add the API key here if necessary)
headers = {
    "Accept": "application/json",
    "X-MBX-SBE": "1:0",
    "X-MBX-APIKEY": api_key  # Include your API key in the header if required
}

response = requests.get("https://api.binance.com/api/v3/exchangeInfo", headers=headers)

if response.status_code == 200:
    data = response.json()
    st.write(data)
else:
    st.error(f"Error fetching data: {response.status_code}")
