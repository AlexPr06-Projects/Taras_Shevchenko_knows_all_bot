import json 
from config import BOT_DATA_CONFIG_FILE_PATH

def load_bot_data_config() -> dict:
    with open(BOT_DATA_CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    