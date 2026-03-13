from aiogram import Router, F, types
from app.utils import bot_answers, BUTTONS, PROPHECIES
import random

router = Router()

@router.message(F.text == BUTTONS["ask_for_prophecy"])
async def give_prophecy_handler(message: types.Message) -> None:
    await message.answer(bot_answers["give_prophecy_text"].replace("{PROPHECY}", random.choice(PROPHECIES)))
    