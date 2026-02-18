![Pylint Status](https://github.com/mmdfathian/TeleBroadcast-Pro/actions/workflows/pylint.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
![Project Status](https://img.shields.io/badge/status-beta-orange)
# 🚀 TeleBroadcast-Pro 
### *Professional Telegram Messaging Automation*

TeleBroadcast-Pro is a high-performance Python tool designed to automate Telegram messaging while strictly adhering to security best practices.

### ⚡ Performance Note
TeleBroadcast-Pro is highly optimized for low-resource environments. 
Current benchmarks show **< 0.0006s** per message processing on a **Samsung A54 (Mobile)**.
## ✨ Features
- **Smart Anti-Spam**: Random sleep intervals (7-15s).
- **Auto Flood-Control**: Handles Telegram's `FloodWait` automatically.
- **Environment Driven**: No hardcoded credentials.
- **External Targets**: Reads recipient lists from `targets.txt`.

## 🛠 Installation
```bash
git clone [https://github.com/your-username/TeleBroadcast-Pro.git](https://github.com/your-username/TeleBroadcast-Pro.git)
cd TeleBroadcast-Pro
pip install -r requirements.txt
