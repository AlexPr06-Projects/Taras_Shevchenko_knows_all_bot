from aiogram import Router, types
from aiogram.filters import CommandStart
from app.utils import bot_answers
from app.keyboards.Reply import get_main_keyboard

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.answer(
        bot_answers["start_text"],
        reply_markup=get_main_keyboard()
    )
    