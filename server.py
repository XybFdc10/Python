import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.1.6"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    try:
        connected = True
        while connected:
            msg_length = conn.recv(HEADER)
            if not msg_length:
                break

            msg_length = int(msg_length.decode(FORMAT).strip())
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("message received".encode(FORMAT))

    except ConnectionResetError:
        print(f"[DISCONNECTED] {addr} force closed the connection")

    finally:
        conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")

print("[STARTING] server is starting")
start()
