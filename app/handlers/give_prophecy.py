from aiogram import Router, F, types
from app.utils import bot_answers
import random
from config import BUTTONS, PROPHECIES

router = Router()

@router.message(F.text == BUTTONS["ask_for_prophecy"])
async def give_prophecy_handler(message: types.Message) -> None:
    await message.answer(bot_answers["give_prophecy_text"].replace("{PROPHECY}", random.choice(PROPHECIES)))