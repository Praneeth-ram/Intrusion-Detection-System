import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
ALERT_LOG_PATH = "../snort/alert.log"

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

def watch_alerts():
    try:
        with open(ALERT_LOG_PATH, "r") as file:
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)
                    continue
                if "[**]" in line:
                    send_alert(f"🚨 Alert Detected:\n{line.strip()}")
    except FileNotFoundError:
        print("❌ Alert log not found!")

if __name__ == "__main__":
    watch_alerts()
