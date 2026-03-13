from aiogram import Router, types

router = Router()

@router.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer("Введи /start щоб розпочати!")
    