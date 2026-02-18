import asyncio
import os
import time
from dotenv import load_dotenv
from tqdm import tqdm
from telethon import TelegramClient
from telethon.errors import FloodWaitError

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
