# Python Socket Chat Project

A simple Python socket programming project for a client-server chat application.

This project supports both terminal-based chat and a simple graphical user interface using Tkinter.

## Features

- Client-server connection
- Multiple clients support with threading
- Broadcast messages
- `/exit` command
- Username support
- Message timestamp
- `/users` command to show connected users
- Private messages with `/pm`
- Simple GUI client with Tkinter
- Basic error handling

## Technologies

- Python
- Socket Programming
- Threading
- Tkinter

## Project Files

~~~text
server.py
client.py
gui_client.py
README.md
.gitignore
~~~

## How to Run

First, make sure Python is installed on your system.

Check Python version:

~~~bash
python --version
~~~

or:

~~~bash
py --version
~~~

## Run the Server

Open a terminal in the project folder and run:

~~~bash
python server.py
~~~

or:

~~~bash
py server.py
~~~

The server will start listening on port `5050`.

## Run the Terminal Client

Open another terminal and run:

~~~bash
python client.py
~~~

or:

~~~bash
py client.py
~~~

To test multiple users, open multiple terminals and run `client.py` in each one.

## Run the GUI Client

To run the graphical client, use:

~~~bash
python gui_client.py
~~~

or:

~~~bash
py gui_client.py
~~~

A simple chat window will open. Enter your username and start chatting.

## Commands

Exit from chat:

~~~text
/exit
~~~

Show connected users:

~~~text
/users
~~~

Send private message:

~~~text
/pm username message
~~~

Example:

~~~text
/pm ali hello ali
~~~

You can also send a private message using IP:

~~~text
/pm 127.0.0.1 hello
~~~

## Project Phases

### Phase 1: Basic Connection

In this phase, a simple connection between the client and the server was created.

The server listens on a specific port, the client connects to the server, sends a message, and receives a response.

### Phase 2: Multiple Clients

In this phase, the server was improved to support multiple clients at the same time using threading.

Each client is handled in a separate thread, so multiple users can connect to the server at the same time.

The server also logs client connection and disconnection with the client IP address.

### Phase 3: Broadcast

In this phase, messages sent by one client are broadcast to other connected clients.

The `/exit` command was also added so clients can leave the chat correctly.

Each message includes the sender IP address.

### Phase 4: Extra Features

In this phase, extra features were added to make the chat application more complete.

Implemented features:

- Username support
- Message timestamp
- `/users` command
- Private message support with `/pm`
- Simple GUI client using Tkinter
- Basic error handling

## Example Usage

Start the server:

~~~bash
python server.py
~~~

Start terminal clients:

~~~bash
python client.py
~~~

Or start GUI clients:

~~~bash
python gui_client.py
~~~

Send a normal message:

~~~text
hello everyone
~~~

Send a private message:

~~~text
/pm ali hello
~~~

Show connected users:

~~~text
/users
~~~

Exit from chat:

~~~text
/exit
~~~

## How It Works

The server creates a socket and waits for clients to connect.

When a client connects, the server creates a new thread for that client. This allows the server to handle multiple clients at the same time.

Each client can send messages to the server. The server then broadcasts public messages to all other connected clients.

For private messages, the server searches for the target user by username or IP address and sends the message only to that user.

The GUI client uses Tkinter to provide a simple graphical interface for sending and receiving messages.

## Git Commit Steps

Suggested commit history:

~~~bash
git add .
git commit -m "initialize socket chat project"
~~~

~~~bash
git add server.py client.py
git commit -m "implement basic client server connection"
~~~

~~~bash
git add server.py client.py
git commit -m "support multiple clients with threading"
~~~

~~~bash
git add server.py client.py
git commit -m "add broadcast chat messages"
~~~

~~~bash
git add server.py client.py
git commit -m "add usernames timestamps and users list"
~~~

~~~bash
git add server.py client.py
git commit -m "add private messages"
~~~

~~~bash
git add gui_client.py
git commit -m "add simple tkinter gui client"
~~~

~~~bash
git add README.md
git commit -m "update project documentation"
~~~

## Author

Name: Saro Hosseini
Course: Computer Networks  
Project: Socket Programming