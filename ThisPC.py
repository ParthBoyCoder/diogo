import socket
import google.generativeai as genai

s = socket.socket()
s.bind(('192.168.0.11', 6969))
s.listen(1)

genai.configure(api_key="KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

print("Waiting for connection...")
conn, addr = s.accept()
print(f"Connected to {addr}")

while True:
    msg = conn.recv(1024).decode()
    if msg == 'q':
        break
    print("Received:", msg)
    
    response = model.generate_content(msg)
    print(response.text)

    conn.send(response.text.encode())

conn.close()