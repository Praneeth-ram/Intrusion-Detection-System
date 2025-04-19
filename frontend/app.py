import streamlit as st
import requests
import time

API_URL = "http://localhost:8000/alerts"

st.set_page_config(page_title="Snort IDS Dashboard", layout="wide")
st.title("Real-Time Intrusion Detection Alerts")

placeholder = st.empty()

while True:
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            alerts = data.get("alerts", [])
            with placeholder.container():
                st.subheader("Recent Alerts")
                for alert in alerts[::-1]:
                    st.markdown(f"- `{alert}`")
        else:
            st.error("Failed to fetch alerts from backend.")
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
    time.sleep(5)
