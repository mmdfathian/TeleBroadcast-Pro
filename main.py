import asyncio
import os
import logging
import random
from dotenv import load_dotenv
from telethon import TelegramClient, errors

# Load environment variables from .env file
load_dotenv()

# --- Advanced Logging Setup ---
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Configuration ---
# These are fetched from your .env file for security
API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
PHONE = os.getenv('TG_PHONE')

async def main():
    """Main function to handle the professional broadcast logic."""
    
    # 1. Validation Check
    if not API_ID or not API_HASH:
        logger.error("❌ API credentials not found! Ensure TG_API_ID and TG_API_HASH are set in .env")
        return

    if not os.path.exists('targets.txt'):
        logger.error("❌ 'targets.txt' file is missing! Please create it and add usernames.")
        return

    # 2. Load Targets
    with open('targets.txt', 'r') as f:
        targets = [line.strip() for line in f if line.strip()]

    if not targets:
        logger.warning("⚠️ The targets.txt file is empty.")
        return

    # Your broadcast message
    message_text = "Hello! This is a professional automated message sent via TeleBroadcast-Pro."

    # 3. Initialize Telegram Client
    # The 'anon_session' file will be created locally to manage your login
    client = TelegramClient('anon_session', API_ID, API_HASH)

    try:
        await client.start(phone=PHONE)
        logger.info("🚀 Connection established. Starting broadcast session...")

        for target in targets:
            try:
                # Sending message to the current target
                await client.send_message(target, message_text)
                logger.info(f"✅ Successfully sent to: {target}")
                
                # Randomized delay to mimic human behavior (Anti-Spam)
                wait_time = random.randint(7, 15)
                logger.info(f"⏳ Waiting for {wait_time} seconds...")
                await asyncio.sleep(wait_time)

            except errors.FloodWaitError as e:
                # Handling Telegram's rate limiting automatically
                logger.warning(f"⚠️ Rate limit hit! Sleeping for {e.seconds}s per Telegram instructions.")
                await asyncio.sleep(e.seconds)
            except errors.UserPrivacyRestrictedError:
                logger.error(f"❌ Cannot send to {target}: Privacy settings restricted.")
            except Exception as e:
                logger.error(f"❌ Failed to send to {target}: {str(e)}")

    except Exception as e:
        logger.critical(f"❗ Unexpected Connection Error: {e}")
    finally:
        await client.disconnect()
        logger.info("🔒 Session closed. Work finished.")

if __name__ == '__main__':
    # Run the asynchronous entry point
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("👋 Process stopped by user.")
