# Intrusion Detection System Dashboard

This project integrates Snort with a FastAPI backend, a Streamlit frontend dashboard, and a Telegram bot for alert notifications.

## Structure
- `backend/`: FastAPI app serving Snort alerts
- `frontend/`: Streamlit dashboard for live alerts
- `monitor/`: Telegram bot scripts for alert notification

## Usage
- Set up Snort and ensure alerts are logged to `/var/log/snort/alert`
- Run backend: `uvicorn main:app --reload`
- Run frontend: `streamlit run app.py`
- Monitor alerts: `python snort_alert_monitor.py` or `telegram_alert.py`

See `monitor/.env.example` for configuring Telegram.
