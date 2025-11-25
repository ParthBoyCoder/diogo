import requests

API_KEY = 'KEY'
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Hiii!"
                }
            ]
        }
    ]
}


response = requests.post(URL, json=payload)
data=response.json()
print(data['candidates'][0]['content']['parts'][0]['text'])