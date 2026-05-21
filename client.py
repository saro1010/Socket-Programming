import socket
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5050
BUFFER_SIZE = 4096


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)

            if not data:
                print("\nConnection closed by server.")
                break

            message = data.decode("utf-8")
            print("\n" + message)
            print("> ", end="", flush=True)

        except OSError:
            break


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    first_message = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    username = input(first_message)
    client_socket.sendall(username.encode("utf-8"))

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client_socket,),
        daemon=True
    )
    receive_thread.start()

    try:
        while True:
            message = input("> ")

            if message == "/exit":
                client_socket.sendall(message.encode("utf-8"))
                break

            client_socket.sendall(message.encode("utf-8"))

    except OSError:
        print("Connection error.")

    finally:
        client_socket.close()


if __name__ == "__main__":
    main()