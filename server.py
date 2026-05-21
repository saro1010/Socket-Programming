import socket
import threading

HOST = "0.0.0.0"
PORT = 5050
BUFFER_SIZE = 4096



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


def handle_client(client_socket, address):
    ip, port = address
    print(f"[CONNECT] Client connected from {ip}:{port}")

    try:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break

            message = data.decode("utf-8")
            print(f"[{ip}:{port}] {message}")

            response = f"پیام شما دریافت شد: {message}"
            client_socket.sendall(response.encode("utf-8"))

    except OSError:
        pass
    finally:
        print(f"[DISCONNECT] Client disconnected from {ip}:{port}")
        client_socket.close()