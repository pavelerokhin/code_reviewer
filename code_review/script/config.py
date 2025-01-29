import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file (if available)
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

if not OPENAI_API_KEY:
    logging.warning("OpenAI API key is missing! Set OPENAI_API_KEY in your environment or .env file.")

# OpenAI Model Configuration
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo").strip()
MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "300"))
TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.3"))

# Project Metadata
PROJECT_NAME = "Code Review Bot"
VERSION = "1.0.0"
