import socket
import threading
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5050
BUFFER_SIZE = 4096

clients = {}
clients_lock = threading.Lock()


def get_time():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender_socket=None):
    with clients_lock:
        all_clients = list(clients.keys())

    for client_socket in all_clients:
        if client_socket == sender_socket:
            continue

        try:
            client_socket.sendall(message.encode("utf-8"))
        except OSError:
            remove_client(client_socket)


def remove_client(client_socket):
    with clients_lock:
        if client_socket in clients:
            del clients[client_socket]

    try:
        client_socket.close()
    except OSError:
        pass


def send_users_list(client_socket):
    with clients_lock:
        users = list(clients.values())

    if not users:
        message = "No users connected."
    else:
        message = "Connected users:\n"
        for user in users:
            message += f"- {user['username']} ({user['ip']})\n"

    client_socket.sendall(message.encode("utf-8"))


def handle_client(client_socket, address):
    ip, port = address
    print(f"[CONNECT] Client connected from {ip}:{port}")

    try:
        client_socket.sendall("Enter your username: ".encode("utf-8"))
        username = client_socket.recv(BUFFER_SIZE).decode("utf-8").strip()

        if username == "":
            username = ip

        with clients_lock:
            clients[client_socket] = {
                "username": username,
                "ip": ip
            }

        join_message = f"[{get_time()}] {username} joined the chat."
        print(join_message)
        broadcast(join_message, sender_socket=client_socket)

        while True:
            data = client_socket.recv(BUFFER_SIZE)

            if not data:
                break

            message = data.decode("utf-8")

            if message == "/exit":
                break

            if message == "/users":
                send_users_list(client_socket)
                continue

            final_message = f"[{get_time()}] {username} ({ip}): {message}"
            print(final_message)

            broadcast(final_message, sender_socket=client_socket)

    except OSError:
        pass

    finally:
        with clients_lock:
            user = clients.get(client_socket)

        if user:
            leave_message = f"[{get_time()}] {user['username']} left the chat."
            print(leave_message)
            broadcast(leave_message, sender_socket=client_socket)

        remove_client(client_socket)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[STARTED] Server is listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, address = server_socket.accept()

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )
            thread.start()

            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    except KeyboardInterrupt:
        print("\n[STOPPED] Server stopped.")

    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()