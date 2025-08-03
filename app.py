import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Replace with your actual API key
API_KEY = os.getenv("IBM_API_KEY")

# Get IAM token
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={
        "apikey": API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

mltoken = token_response.json()["access_token"]

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + mltoken
}

# Payload: replace "Why is my op-amp oscillating?" with any prompt
payload_scoring = {
    "input": {
        "message_type": "text",
        "text": "Why is my op-amp oscillating?"
    }
}

# Endpoint: use ai_service (not ai_service_stream unless streaming)
url = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5b4ae951-ace1-46da-b876-f2ede9e20e02/ai_service?version=2021-05-01"

# Send request
response = requests.post(url, json=payload_scoring, headers=headers)

# Print response
print("Scoring response:")
try:
    print(response.json())
except ValueError:
    print(response.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
