# TCP Chat App 💬

A simple multi-client chat application using TCP sockets in Python. Includes real-time messaging, timestamps, and admin moderation features.

---

## 🚀 Features

- 🔗 TCP-based client-server communication
- 🧍‍♀️ Multiple clients can join the same server
- ⏰ Timestamps for every message
- 🛡 Admin features:
  - `/kick <username>` to remove users from the chat
- ⚙️ Separate threads for sending & receiving messages
- 🌈 Clean and readable message formatting

---

## 🛠 Tech Stack

- **Python 3**
- `socket` (for network communication)
- `threading` (for concurrency)
- `datetime` (for timestamps)
- `colorama` (for optional colored client output)

---

## 📦 Requirements

- Python 3.x
- `colorama` (optional):

```bash
pip install colorama
