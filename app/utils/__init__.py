from . import load_answers, load_data_config

bot_answers = load_answers.load_bot_answers()
bot_data_config = load_data_config.load_bot_data_config()

BUTTONS = bot_data_config["buttons"]
PROPHECIES = bot_data_config["prophecies"]
