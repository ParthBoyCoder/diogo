import socket

s = socket.socket()
s.connect(('192.168.0.11', 6969))

while True:
    msg = input("Send: ")
    s.send(msg.encode())
    if msg == 'q':
        break
    reply = s.recv(1024).decode()
    print("Reply:", reply)

s.close()