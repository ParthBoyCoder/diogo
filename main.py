import base64
import requests
import wget
import RPi.GPIO as gpio
import time
import os

file=open("data.txt", "a+")
data=file.read()

angle=90

running=True
prompt=f"""
These r ur previous messages. Follow the first command and see what u said (You: ur msg) for context. ur new angles are updated (ur current angle: angle)

Hi, you can see the real world. the attached image is ur vision. ur eye can be moved left if u include "left123".
u can move your eye in the right direction if u say "right123". dont output both at the same time. if and only if u want to quit, say quit123.
dont say quit123 if u dont want to quit. left123 move u -10 degree and right123 moves u +10 degree. u can only move between 0 and 180, dont try to move beyond that.
ur current angle is {angle}. Also describe what u see along with the code (left123, right123 or quit123).



"""

file.write(prompt)

pin=12
duty=0

gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT)

pwm=gpio.PWM(12, 50)
pwm.start(0)

API_KEY = 'KEY'
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

wget.download('http://192.168.0.21/capture')

def set_angle(angle):
    duty=2+(angle/18)
    gpio.output(12,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.4)
    gpio.output(12,gpio.LOW)
    pwm.ChangeDutyCycle(0)

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

image_b64 = image_to_base64("capture.jpg")

def gem(prm, img):
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prm
                    },
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": img
                        }
                    }
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(URL, headers=headers, json=payload)
    data=response.json()
    return (data['candidates'][0]['content']['parts'][0]['text'])

#print(gem(prompt, image_b64))

while running:
    out=gem(prompt, image_b64) #prompt-> file.read()
    
    print()

    print(out)

    if "right123" in out:
        angle+=10
    elif "left123" in out:
        angle-=10
    elif "quit123":   #in out
        running=False

    print(angle)

    file.write("You: " +  out + f"""

    ur current angle: {angle}

    """)    

    set_angle(angle)

    os.remove("capture.jpg")
    wget.download('http://192.168.0.21/capture', "capture.jpg")
    image_b64 = image_to_base64("capture.jpg")

    time.sleep(0.5)