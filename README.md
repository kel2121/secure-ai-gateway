# Secure AI Gateway

A FastAPI-based backend service that analyzes text input and assigns a risk score based on suspicious patterns. Designed as a lightweight AI security middleware for filtering unsafe prompts before reaching large language models.

## Features
- Detects suspicious keywords and patterns
- Assigns dynamic risk score (0–100)
- Flags potentially harmful inputs
- Logs flagged requests
- REST API built with FastAPI
- Interactive Swagger UI documentation

## Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Git & GitHub

## How It Works
1. User sends text to `/analyze`
2. Text is scanned for suspicious patterns
3. Risk score is calculated
4. Response returns:
   - risk_score
   - status (safe / flagged)

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload