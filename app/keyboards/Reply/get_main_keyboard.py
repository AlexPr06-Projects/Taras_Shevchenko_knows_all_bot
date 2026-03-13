from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import BUTTONS

def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    for button in BUTTONS.values():
        builder.row(types.KeyboardButton(text=button))

    return builder.as_markup(resize_keyboard=True)
