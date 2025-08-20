import socket

HOST = "0.0.0.0"   # listen on all interfaces
PORT = 8888        # pick any open port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(1)
    print(f"listening on {HOST}:{PORT} ...")
    conn, addr = srv.accept()
    print("connected from", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("peer:", data.decode(errors="ignore"))
            # optional echo back
            conn.sendall(b"ACK: " + data)
