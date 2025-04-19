import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SNORT_ALERT_LOG = "/var/log/snort/alert"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"[SENT] Telegram alert: {message}")
        else:
            print(f"[ERROR] Telegram failed with code: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Telegram exception: {e}")

def monitor_snort_alerts():
    try:
        with open(SNORT_ALERT_LOG, "r") as log:
            log.seek(0, 2)
            print("[INFO] Monitoring Snort alerts...")
            while True:
                line = log.readline()
                if line and "[**]" in line:
                    print(f"[ALERT] {line.strip()}")
                    send_telegram_alert(line.strip())
                time.sleep(1)
    except FileNotFoundError:
        print(f"[ERROR] Alert log file not found: {SNORT_ALERT_LOG}")

if __name__ == "__main__":
    monitor_snort_alerts()
