import socket

HOST = "0.0.0.0"
PORT = 5050
BUFFER_SIZE = 4096



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    client_socket, address = server_socket.accept()
    print(f"Client connected from {address}")

    data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("Client:", data)

    client_socket.sendall("سلام کلاینت!".encode("utf-8"))

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()