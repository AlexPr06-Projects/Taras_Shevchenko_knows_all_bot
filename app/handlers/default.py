from aiogram import Router, types
from app.utils import bot_answers

router = Router()

@router.message()
async def default_handler(message: types.Message) -> None:
    await message.answer(bot_answers["default_text"])
    