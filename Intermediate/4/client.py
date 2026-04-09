import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5555

def receive_messages(sock):
    """Continuously listen for incoming messages and print them."""
    while True:
        try:
            message = sock.recv(1024).decode().strip()
            if not message:
                print("[Disconnected from server]")
                break
            # Print on its own line without interrupting the user's typing
            print(f"\r{message}\n> ", end="", flush=True)
        except (ConnectionResetError, OSError):
            print("[Disconnected from server]")
            break

def main():
    username = input("Enter your username: ").strip()
    if not username:
        print("Username cannot be empty.")
        sys.exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f"Could not connect to {HOST}:{PORT}. Is the server running?")
        sys.exit(1)

    # Send username to the server as the first message
    sock.send(username.encode())

    # Start background thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(sock,))
    thread.daemon = True
    thread.start()

    print(f"Connected! Type your message and press Enter. (Ctrl+C to quit)\n")

    try:
        while True:
            message = input("> ").strip()
            if message:
                sock.send(message.encode())
    except KeyboardInterrupt:
        print("\n[Leaving chat]")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
