import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5050
BUFFER_SIZE = 4096


class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Socket Chat")
        self.root.geometry("500x500")

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.chat_box = tk.Text(root, state="disabled")
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.message_entry = tk.Entry(root)
        self.message_entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=(0, 10), fill=tk.X)

        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect((SERVER_HOST, SERVER_PORT))

            first_message = self.client_socket.recv(BUFFER_SIZE).decode("utf-8")

            username = simpledialog.askstring("Username", first_message)

            if username is None or username.strip() == "":
                username = "GUI_User"

            self.client_socket.sendall(username.encode("utf-8"))

            receive_thread = threading.Thread(
                target=self.receive_messages,
                daemon=True
            )
            receive_thread.start()

            self.show_message("Connected to server.")

        except OSError:
            messagebox.showerror("Connection Error", "Could not connect to server.")
            self.root.destroy()

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(BUFFER_SIZE)

                if not data:
                    self.show_message("Connection closed by server.")
                    break

                message = data.decode("utf-8")
                self.show_message(message)

            except OSError:
                break

    def send_message(self, event=None):
        message = self.message_entry.get().strip()

        if message == "":
            return

        try:
            self.client_socket.sendall(message.encode("utf-8"))

            if message == "/exit":
                self.close_window()
                return

            self.message_entry.delete(0, tk.END)

        except OSError:
            self.show_message("Message could not be sent.")

    def show_message(self, message):
        self.chat_box.config(state="normal")
        self.chat_box.insert(tk.END, message + "\n")
        self.chat_box.config(state="disabled")
        self.chat_box.see(tk.END)

    def close_window(self):
        try:
            self.client_socket.sendall("/exit".encode("utf-8"))
            self.client_socket.close()
        except OSError:
            pass

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()