# TCP Chat App 💬

A simple multi-client chat application using TCP sockets in Python. Includes real-time messaging, timestamps, and admin moderation features.

---

## 🚀 Features

- 🔗 TCP-based client-server communication  
- 🧍‍♀️ Multiple clients can join the same server  
- ⏰ Timestamps for every message  
- 🛡️ Admin features:  
  - `/kick <username>` to remove users from the chat  
- ⚙️ Separate threads for sending & receiving messages  
- 🌈 Clean and readable message formatting  

---

## 🛠 Tech Stack

- **Python 3**
- `socket` (for network communication)
- `threading` (for concurrency)
- `datetime` (for timestamps)
- `colorama` (optional; for colored terminal output)

---

## 📦 Requirements

- Python 3.x  
- Install `colorama` (optional):

```bash
pip install colorama
---

## 🖥 How to Run

### 1. Start the Server:
```bash
python server.py

### 2. Start the Client:
```bash
python client.py
### 3. Admin mode:
```bash
/kick <username>


