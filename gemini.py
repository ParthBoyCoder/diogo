import base64
import requests

API_KEY = 'KEY'
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"


def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

image_b64 = image_to_base64("jota.jpeg")

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Who is the player shown in the image?"
                },
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": image_b64
                    }
                }
            ]
        }
    ]
}

headers = {"Content-Type": "application/json"}
response = requests.post(URL, headers=headers, json=payload)
data=response.json()
print(data['candidates'][0]['content']['parts'][0]['text'])