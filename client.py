import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5050
BUFFER_SIZE = 4096


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    try:
        while True:
            message = input("> ")

            if message == "/exit":
                break

            client_socket.sendall(message.encode("utf-8"))

            response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
            print("Server:", response)

    finally:
        client_socket.close()    


if __name__ == "__main__":
    main()