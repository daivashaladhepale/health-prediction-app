import os
from dotenv import load_dotenv
import requests

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")


def fallback_prediction(glucose, haemoglobin, cholesterol):

    if glucose > 140 and cholesterol > 240:
        return (
            "Patient may be at risk of diabetes and high cholesterol. "
            "Medical consultation is recommended."
        )

    elif glucose > 140:
        return (
            "Patient may be at risk of diabetes due to elevated glucose levels."
        )

    elif cholesterol > 240:
        return (
            "Patient may be at risk of cardiovascular issues due to high cholesterol."
        )

    elif haemoglobin < 12:
        return (
            "Patient may be at risk of anemia due to low haemoglobin levels."
        )

    return (
        "Blood test values appear to be within normal ranges."
    )


def predict_health(glucose, haemoglobin, cholesterol):

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.2-3b-instruct:free",
                "messages": [
                    {
                        "role": "user",
                        "content": f"""
You are a healthcare assistant.

Patient Report:

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Provide a short health risk assessment in 1 sentence.
"""
                    }
                ]
            },
            timeout=30
        )

        print("OpenRouter Status:", response.status_code)

        if response.status_code == 200:

            data = response.json()

            ai_remark = (
                data["choices"][0]
                ["message"]
                ["content"]
            )

            return ai_remark

        print("OpenRouter Response:", response.text)

        return fallback_prediction(
            glucose,
            haemoglobin,
            cholesterol
        )

    except Exception as e:

        print("OpenRouter Error:", e)

        return fallback_prediction(
            glucose,
            haemoglobin,
            cholesterol
        )