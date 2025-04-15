import socket
import threading
from colorama import Fore, Style, init

init()

username = input("Enter your username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "USERNAME":
                client.send(username.encode('utf-8'))
            elif message.startswith("You were kicked"):
                print(Fore.RED + message + Style.RESET_ALL)
                client.close()
                break
            else:
                if "] " in message and ":" in message:
                    timestamp_split = message.split("] ", 1)
                    timestamp = timestamp_split[0] + "]"
                    name_msg = timestamp_split[1]
                    if ":" in name_msg:
                        sender, content = name_msg.split(":", 1)
                        print(f"{Fore.GREEN}{timestamp} {Fore.CYAN}{sender}:{Style.RESET_ALL}{content}")
                    else:
                        print(message)
                else:
                    print(message)
        except:
            print("An error occurred. Closing connection.")
            client.close()
            break

def write_messages():
    while True:
        try:
            message = input("")
            if message.strip() == "":
                continue 
            full_message = f'{message}' if message.startswith("/") else f'{username}: {message}'
            client.send(full_message.encode('utf-8'))
        except:
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()
