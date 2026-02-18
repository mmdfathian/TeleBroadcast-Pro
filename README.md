![Pylint Status](https://github.com/mmdfathian/TeleBroadcast-Pro/actions/workflows/pylint.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.10-blue)
![Project Status](https://img.shields.io/badge/status-beta-orange)

# 🚀 TeleBroadcast-Pro 
### *Professional Telegram Messaging Automation*

TeleBroadcast-Pro is a high-performance Python tool designed to automate Telegram messaging while strictly adhering to security best practices and rate-limiting stability.

## ⚡ Performance & Efficiency
TeleBroadcast-Pro is engineered for high-speed execution. We use `time.perf_counter()` to ensure the core logic remains lightning-fast across all environments.

### Latest Benchmark Results
* **Cloud Performance (GitHub Actions):** ~0.000594s per message processing.
* **Capacity:** Capable of processing millions of records per second on server-grade hardware.
* **Mobile Performance:** Optimized for architectures like Samsung A54 (Exynos 1380).

## ✨ Features (Comprehensive List)
- **Visual Progress Bar**: Real-time status tracking using `tqdm` for a better user experience.
- **Auto Flood-Control**: Smart handling of Telegram's `FloodWaitError` (Wait & Retry logic).
- **Smart Anti-Spam**: Random and fixed safety delays to mimic human behavior and protect accounts.
- **Environment Driven**: Zero hardcoded credentials; uses `.env` files for maximum security.
- **High-Resolution Benchmarking**: Internal tool to measure hardware processing speed.
- **Session Management**: Secure handling of Telegram sessions without repeated logins.
- **Modular Design**: Clean, refactored code for easy maintenance and scalability.

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mmdfathian/TeleBroadcast-Pro.git](https://github.com/mmdfathian/TeleBroadcast-Pro.git)
   cd TeleBroadcast-Pro
