"""Module for handling Telegram broadcasting logic and flood control."""
import asyncio
from tqdm import tqdm
from telethon.errors import FloodWaitError
from logger_utils import get_logger

logger = get_logger("Broadcaster")

async def send_broadcast(client, user_id, message):
    """Sends a single message to a user and logs the result."""
    try:
        await client.send_message(user_id, message)
        logger.info("SUCCESS: Message sent to %s", user_id)
        return True
    except Exception as err:  # pylint: disable=broad-exception-caught
        logger.error("FAILED: Could not send to %s. Details: %s", user_id, err)
        return False

async def start_broadcast(client, user_ids, message):
    """Iterates through user list and sends messages with safety delays."""
    logger.info("Starting broadcast to %s users...", len(user_ids))
    
    for user in tqdm(user_ids, desc="Progress", unit="msg"):
        try:
            await client.send_message(user, message)
            await asyncio.sleep(0.5)
            
        except FloodWaitError as e:
            logger.warning("Flood alert! Sleeping for %s seconds...", e.seconds)
            await asyncio.sleep(e.seconds)
            await client.send_message(user, message)

        except Exception as err:  # pylint: disable=broad-exception-caught
            logger.error("Error for user %s: %s", user, err)
            continue

    logger.info("Broadcast completed successfully.")
