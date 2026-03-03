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
    try:
        risk_score = analyze_text(input_data.text)

        if risk_score < 30:
            risk_level = "low"
            status = "allowed"
        elif risk_score < 70:
            risk_level = "medium"
            status = "flagged"
        else:
            risk_level = "high"
            status = "blocked"

        log_entry = f"{datetime.datetime.now()} | {input_data.text} | {risk_score} | {risk_level}\n"

        with open("security_logs.txt", "a") as log_file:
            log_file.write(log_entry)

        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
            "status": status
        }

    except Exception as e:
        return {"error": str(e)}