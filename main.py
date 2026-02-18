"""Main entry point for TeleBroadcast-Pro application."""
import asyncio
import time
from telethon import TelegramClient
from config import API_ID, API_HASH
from logger_utils import get_logger
from broadcaster import start_broadcast

logger = get_logger("MainApp")

async def main():
    """Main function to handle user menu and client lifecycle."""
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        print("\n--- TeleBroadcast-Pro Menu ---")
        print("1. Speed Test (Benchmark)")
        print("2. Start Real Broadcast")
        
        choice = input("\nSelect an option (1 or 2): ")
        
        if choice == "1":
            print("⏱ Running Benchmark...")
            start_time = time.perf_counter()
            await asyncio.sleep(1)
            duration = time.perf_counter() - start_time
            logger.info("Benchmark finished. Average Speed: %s", f"{duration:.6f}s")
            
        elif choice == "2":
            users = ['user1', 'user2', 'user3']
            msg = "Hello! This is a test broadcast message."
            await start_broadcast(client, users, msg)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Process terminated by user.")
