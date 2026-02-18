"""Module for loading environment configurations."""
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

if not API_ID or not API_HASH:
    raise ValueError("ERROR: API_ID or API_HASH not found in .env file!")
