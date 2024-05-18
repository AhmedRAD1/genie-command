import requests
import json
import sys

# Define the URL and the API key
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'

api_key = 'AIzaSyAFwMClSQMuASh7McgWyhyNsxZrvE5IaCw'

text = ""
if len(sys.argv) > 1:

    text ="Only answer if the question is about bash:"+ sys.argv[1]
else:
    exit()

# Define the headers and the payload
headers = {
    'Content-Type': 'application/json'
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text":text
                }
            ]
        }
    ]
}

# Make the POST request
response = requests.post(f'{url}?key={api_key}', headers=headers, data=json.dumps(payload))

# Print the response
data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
#access the generating text
print(data)
