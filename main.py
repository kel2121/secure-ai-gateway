from fastapi import FastAPI
from pydantic import BaseModel
import re
import datetime

app = FastAPI()

class InputText(BaseModel):
    text: str

# your analyze_text function
def analyze_text(text: str) -> int:
    suspicious_patterns = [
        r"hack",
        r"bank",
        r"steal",
        r"phish",
        r"password",
        r"bypass",
        r"exploit",
        r"ddos",
        r"malware"
    ]

    score = 0
    lower = text.lower()

    for pattern in suspicious_patterns:
        if re.search(pattern, lower):
            score += 20

    return min(score, 100)
@app.post("/analyze")
def analyze(input_data: InputText):
    
    risk_score = analyze_text(input_data.text)

    # Determine risk level
    if risk_score == 0:
        risk_level = "Low"
        status = "safe"
    elif risk_score <= 40:
        risk_level = "Medium"
        status = "flagged"
    else:
        risk_level = "High"
        status = "flagged"

    log_entry = f"{datetime.datetime.now()} | Risk Score: {risk_score} | Risk Level: {risk_level} | Text: {input_data.text}\n"

    with open("security_logs.txt", "a") as log_file:
        log_file.write(log_entry)

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "status": status
    }