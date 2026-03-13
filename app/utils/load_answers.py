from config import BOT_ANSWERS_FILE_PATH
import json

def load_bot_answers() -> dict:
    with open(BOT_ANSWERS_FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    