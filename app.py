
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable for security
API_KEY = os.getenv("IBM_API_KEY")

def get_watson_response(user_question):
    if not API_KEY:
        return "Error: IBM_API_KEY not found in environment variables"

    try:
        # Get access token
        token_response = requests.post(
            'https://iam.cloud.ibm.com/identity/token', 
            data={
                "apikey": API_KEY, 
                "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'
            }
        )
        token_response.raise_for_status()
        mltoken = token_response.json()["access_token"]
    except requests.exceptions.RequestException as e:
        return f"Error getting access token: {e}"
    except KeyError:
        return "Error: Invalid API key or response format"

    # Set up headers
    header = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + mltoken
    }

    # Properly formatted payload with actual content
    payload_scoring = {
        "messages": [
            {
                "content": user_question,
                "role": "user"
            }
        ]
    }

    try:
        response_scoring = requests.post(
            'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5b4ae951-ace1-46da-b876-f2ede9e20e02/ai_service_stream?version=2021-05-01', 
            json=payload_scoring,
            headers=header,
            stream=True
        )
        
        if response_scoring.status_code == 200:
            full_response = ""
            
            # Parse Server-Sent Events stream
            for line in response_scoring.iter_lines(decode_unicode=True):
                if line.startswith('data: '):
                    try:
                        data_str = line[6:]
                        if data_str.strip() == '[DONE]':
                            break
                        if data_str.strip():
                            data = json.loads(data_str)
                            
                            if 'choices' in data and len(data['choices']) > 0:
                                delta = data['choices'][0].get('delta', {})
                                content = delta.get('content', '')
                                if content:
                                    full_response += content
                                    
                    except json.JSONDecodeError:
                        continue
            
            return full_response
        else:
            try:
                error_details = response_scoring.json()
                return f"HTTP Error {response_scoring.status_code}: {error_details}"
            except ValueError:
                return f"HTTP Error {response_scoring.status_code}: {response_scoring.text}"
                
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def main():
    print("Watson AI Assistant - Audio Signal Processing")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        user_input = input("\nYour question: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
            
        if not user_input:
            print("Please enter a question.")
            continue
            
        print("\nWatson is thinking...")
        response = get_watson_response(user_input)
        print(f"\nWatson: {response}")

if __name__ == '__main__':
    main()
