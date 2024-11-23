import os
import json
import requests
import streamlit as st

# Đường dẫn tới file config.json
config_path = "config.json"

# Tạo cấu hình mặc định để tránh lỗi khi không tìm thấy file
default_config = {
    "api_key": "default_api_key",
    "api_secret": "default_api_secret"
}

# Hàm để tải cấu hình
def load_config(config_path):
    if not os.path.exists(config_path):
        st.error("Config file not found! Using default configuration.")
        return default_config
    elif os.path.getsize(config_path) == 0:
        st.error("Config file is empty! Using default configuration.")
        return default_config
    else:
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                st.success("Config loaded successfully!")
                return config
        except json.JSONDecodeError as e:
            st.error(f"JSON decode error: {e}")
            return default_config

# Tải cấu hình
config = load_config(config_path)

# Sử dụng API key từ file config
api_key = config.get("api_key")
api_secret = config.get("api_secret")

# Header cho yêu cầu API
headers = {
    "Accept": "application/json",
    "X-MBX-SBE": "1:0",
    "X-MBX-APIKEY": api_key  # Thêm API key vào header nếu cần
}

# Gửi yêu cầu tới Binance API
try:
    response = requests.get("https://api.binance.com/api/v3/exchangeInfo", headers=headers)
    if response.status_code == 200:
        data = response.json()
        st.write(data)  # Hiển thị dữ liệu nhận được từ API
    else:
        st.error(f"Error fetching data: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    st.error(f"An error occurred while making the request: {e}")
