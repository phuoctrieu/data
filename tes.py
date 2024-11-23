import requests
import streamlit as st

headers = {
    "Accept": "application/json",
    "X-MBX-SBE": "1:0"
}
response = requests.get("https://api.binance.com/api/v3/exchangeInfo", headers=headers)

if response.status_code == 200:  # Kiểm tra trạng thái phản hồi
    data = response.json()
    st.write(data)  # Hiển thị dữ liệu nhận được
else:
    st.error(f"Error fetching data: {response.status_code}")