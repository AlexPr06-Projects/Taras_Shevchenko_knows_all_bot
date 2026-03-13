import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Loading configs from .env
#TODO: Create loading logic
TOKEN = os.getenv("TOKEN")

# Directories & Paths
BASE_DIR = Path(__file__).resolve().parent

BOT_ANSWERS_FILE_PATH = BASE_DIR / "data/bot_answers.json"
BOT_DATA_CONFIG_FILE_PATH = BASE_DIR / "data/config.json"

APP_DIR = BASE_DIR / "app"
HANDLERS_DIR = APP_DIR / "handlers"
KEYBOARDS_DIR = APP_DIR / "keyboards"
MIDDLEWARES_DIR = APP_DIR / "middlewares"
UTILS_DIR = APP_DIR / "utils"


# Allowed updates
ALLOWED_UPDATES = [
    'message', 
    'callback_query'
]
