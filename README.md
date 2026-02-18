![Pylint Status](https://github.com/mmdfathian/TeleBroadcast-Pro/actions/workflows/pylint.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
![Project Status](https://img.shields.io/badge/status-beta-orange)
# 🚀 TeleBroadcast-Pro 
### *Professional Telegram Messaging Automation*

TeleBroadcast-Pro is a high-performance Python tool designed to automate Telegram messaging while strictly adhering to security best practices.

## ⚡ Performance & Efficiency

TeleBroadcast-Pro is engineered for high-speed execution and minimal resource consumption. We continuously monitor performance across different environments.

### Latest Benchmark Results
Tests are conducted using our internal benchmarking tool to ensure the core logic remains lightning-fast.

* **Cloud Performance (GitHub Actions):** * **Message Formatting:** ~0.000594s per 5k batch.
    * **Capacity:** Capable of processing millions of records per second on server-grade hardware.
* **Mobile Performance (Baseline):** * Optimized to run smoothly on mobile architectures (like Samsung A54), making it ideal for low-power VPS or handheld terminal execution.

> [!TIP]
> For a detailed breakdown of the testing hardware (CPU, RAM, and OS), please refer to our [Environment Report](benchmarks/ENVIRONMENT.md).

### How we measure?
We use `time.perf_counter()` to capture high-resolution timing and calculate averages over 100+ iterations to eliminate anomalies.
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
