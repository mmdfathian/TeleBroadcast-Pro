import asyncio
import time
from tqdm import tqdm
from telethon.errors import FloodWaitError
from logger_utils import get_logger

logger = get_logger("Broadcaster")

async def send_broadcast(client, user_id, message):
    try:
        await client.send_message(user_id, message)
        logger.info(f"SUCCESS: Message sent to {user_id}")
        return True
    except Exception as e:
        logger.error(f"FAILED: Could not send to {user_id}. Details: {e}")
        return False

async def start_broadcast(client, user_ids, message):
    logger.info(f"Starting broadcast to {len(user_ids)} users...")
    
    for user in tqdm(user_ids, desc="Progress", unit="msg"):
        try:
            await client.send_message(user, message)
            await asyncio.sleep(0.5) # Anti-spam delay
            
        except FloodWaitError as e:
            logger.warning(f"Flood alert! Sleeping for {e.seconds} seconds...")
            await asyncio.sleep(e.seconds)
            await client.send_message(user, message) 

        except Exception as e:
            logger.error(f"Error for user {user}: {e}")
            continue

    logger.info("Broadcast completed successfully.")
