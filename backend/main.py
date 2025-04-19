from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_PATH = "/var/log/snort/alert"  # adjust as needed

@app.get("/alerts")
def get_alerts(limit: int = 20):
    if not os.path.exists(LOG_PATH):
        return {"error": "Alert log not found"}
    
    with open(LOG_PATH, "r") as file:
        lines = file.readlines()
    
    alerts = [line.strip() for line in lines if "[**]" in line]
    return {"alerts": alerts[-limit:]}  # return last `limit` alerts
