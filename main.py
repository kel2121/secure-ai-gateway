from fastapi import FastAPI
from pydantic import BaseModel
import re
import datetime

app = FastAPI()

class InputText(BaseModel):
    text: str

suspicious_patterns = [
    r"bypass",
    r"ignore previous",
    r"override",
    r"disable safety",
    r"exploit",
]

def analyze_text(text):
    score = 0
    for pattern in suspicious_patterns:
        if re.search(pattern, text.lower()):
            score += 20
    return min(score, 100)

@app.post("/analyze")
def analyze(input_data: InputText):
    risk_score = analyze_text(input_data.text)

    log_entry = f"{datetime.datetime.now()} | Risk Score: {risk_score} | Text: {input_data.text}\n"

    with open("security_logs.txt", "a") as log_file:
        log_file.write(log_entry)

    return {
        "risk_score": risk_score,
        "status": "flagged" if risk_score > 0 else "safe"
    }