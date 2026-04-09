import socket
import threading

HOST = "0.0.0.0"
PORT = 5555

# Keep track of every connected client socket and its username
clients = {}   # {socket: username}

def broadcast(message, sender=None):
    """Send a message to all connected clients except the sender."""
    for client in list(clients):
        if client is not sender:
            try:
                client.send(message.encode())
            except:
                remove_client(client)

def remove_client(client):
    """Disconnect a client and clean up."""
    if client in clients:
        username = clients.pop(client)
        client.close()
        broadcast(f"[Server] {username} has left the chat.")
        print(f"[-] {username} disconnected.")

def handle_client(client, address):
    """Run in a separate thread for each connected client."""
    try:
        # First message from client must be their username
        username = client.recv(1024).decode().strip()
        clients[client] = username
        print(f"[+] {username} connected from {address}")
        broadcast(f"[Server] {username} has joined the chat.", sender=client)
        client.send("[Server] Welcome! You are now connected.\n".encode())

        # Listen for messages until the client disconnects
        while True:
            message = client.recv(1024).decode().strip()
            if not message:
                break
            print(f"[{username}] {message}")
            broadcast(f"[{username}] {message}", sender=client)

    except (ConnectionResetError, OSError):
        pass
    finally:
        remove_client(client)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow re-binding the port immediately after restart
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[Server] Listening on {HOST}:{PORT} ...")

    try:
        while True:
            client, address = server.accept()
            # Each client gets its own thread so they don't block each other
            thread = threading.Thread(target=handle_client, args=(client, address))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("\n[Server] Shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    main()
