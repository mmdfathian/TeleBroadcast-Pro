import asyncio
import os
import time
from dotenv import load_dotenv
from tqdm import tqdm
from telethon import TelegramClient
from telethon.errors import FloodWaitError
import logging
import os
from datetime import datetime

# Logging Configuration
log_filename = f"broadcast_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler()  # Display in terminal
    ]
)

logger = logging.getLogger(__name__)

# Usage Example inside your functions:
async def send_broadcast(client, user_id, message):
    try:
        await client.send_message(user_id, message)
        logger.info(f"SUCCESS: Message sent to {user_id}")
        return True
    except Exception as e:
        logger.error(f"FAILED: Could not send to {user_id}. Details: {e}")
        return False

# 1. Load configuration from .env file
load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# 2. Smart Broadcast Function with Progress Bar and Flood Control
async def start_broadcast(client, user_ids, message):
    print(f"\n📢 Starting broadcast to {len(user_ids)} users...")
    
    # Progress bar initialization
    for user in tqdm(user_ids, desc="Progress", unit="msg"):
        try:
            await client.send_message(user, message)
            # Small delay to keep the account safe
            await asyncio.sleep(0.5) 
            
        except FloodWaitError as e:
            # Handle Telegram rate limits automatically
            print(f"\n⚠️ Flood alert! Sleeping for {e.seconds} seconds...")
            await asyncio.sleep(e.seconds)
            await client.send_message(user, message) # Retry after sleep

        except Exception as e:
            # Skip invalid users and continue
            continue

    print("\n✅ Broadcast completed successfully.")

# 3. Main Application Logic
async def main():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        print("1. Speed Test (Benchmark)")
        print("2. Start Real Broadcast")
        
        choice = input("\nSelect an option (1 or 2): ")
        
        if choice == "1":
            # Speed testing logic (from Day 1)
            print("⏱ Running Benchmark...")
            start_time = time.perf_counter()
            # ... (Benchmark logic goes here)
            print(f"Average Speed: {time.perf_counter() - start_time:.6f}s")
            
        elif choice == "2":
            # List of target users (Replace with real IDs/Usernames)
            users = ['user1', 'user2', 'user3'] 
            msg = "Hello! This is a test broadcast message."
            await start_broadcast(client, users, msg)

if __name__ == '__main__':
    asyncio.run(main())
