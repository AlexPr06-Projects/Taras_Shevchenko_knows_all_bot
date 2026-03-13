from aiogram import Router, F, types
from app.utils import bot_answers
from config import BUTTONS

router = Router()

@router.message(F.text == BUTTONS["stop"])
async def close_menu_handler(message: types.Message) -> None:
    await message.answer(
        bot_answers["stop_text"],
        reply_markup=types.ReplyKeyboardRemove()
    )