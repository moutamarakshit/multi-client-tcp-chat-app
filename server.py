import socket
import threading
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()

clients = []
usernames = []
admin_username = "moutama"  

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            decoded_msg = message.decode('utf-8')
            sender = usernames[clients.index(client)]

            
            if decoded_msg.startswith("/kick") and sender == admin_username:
                target_name = decoded_msg.split(" ")[1]
                if target_name in usernames:
                    target_index = usernames.index(target_name)
                    target_client = clients[target_index]
                    target_client.send("You were kicked by the admin.".encode('utf-8'))
                    target_client.close()
                    clients.remove(target_client)
                    usernames.remove(target_name)
                    timestamp = datetime.now().strftime("%H:%M")
                    broadcast(f"[{timestamp}] {target_name} was kicked by the admin!".encode('utf-8'))
                else:
                    client.send("User not found.".encode('utf-8'))
            else:
                timestamp = datetime.now().strftime("%H:%M")
                broadcast(f"[{timestamp}] {sender}: {decoded_msg}".encode('utf-8'))

        except:
            index = clients.index(client)
            client.close()
            username = usernames[index]
            clients.remove(client)
            usernames.remove(username)
            timestamp = datetime.now().strftime("%H:%M")
            broadcast(f"[{timestamp}] {username} left the chat.".encode('utf-8'))
            break

def receive_connections():
    print("Server started on 127.0.0.1:55555 and is listening...")

    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')

        usernames.append(username)
        clients.append(client)

        timestamp = datetime.now().strftime("%H:%M")
        print(f"Username is {username}")
        broadcast(f"[{timestamp}] {username} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
