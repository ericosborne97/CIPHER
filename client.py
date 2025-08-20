import socket

SERVER_IP = "192.168.49.1"  # replace with the server’s IP
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, PORT))
    print("connected to", SERVER_IP, PORT)
    while True:
        msg = input("> ")
        if not msg:
            break
        s.sendall(msg.encode())
        # optional read server echo:
        reply = s.recv(1024)
        if not reply:
            break
        print("reply:", reply.decode(errors="ignore"))
