from aiogram import Router, F, types
from app.utils import bot_answers, BUTTONS

router = Router()

@router.message(F.text == BUTTONS["start"])
async def greet_handler(message: types.Message) -> None:
    await message.answer(bot_answers["greet_text"].replace("{USERNAME}", message.from_user.full_name))
