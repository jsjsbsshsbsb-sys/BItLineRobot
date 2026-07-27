from aiogram.types import CallbackQuery
from aiogram import Router, F
import json

from keyboards.menu import create_menu
from keyboards.back_kb import create_back_kb


router = Router()

DATABASE_PATH = "core/db.json"


@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery):

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        database = json.load(file)


    user = None
    local_id = None


    # поиск по Telegram ID
    for user_id, user_data in database["users"].items():

        if user_data["telegram_id"] == callback.from_user.id:
            user = user_data
            local_id = user_id
            break


    if user:

        text = (
            f"Ваш профиль:\n\n"
            f"Системный ID: {local_id}\n"
            f"Телеграмм ID: {user['telegram_id']}\n"
            f"Имя: {user['name']}\n"
            f"Баланс: {user['balance']}\n"
        )

    else:

        text = (
            "❌ По неизвестной причине вас нет в базе данных!\n"
            "Обратитесь в поддержку!"
        )


    await callback.message.edit_caption(
        caption=text,
        reply_markup=create_back_kb()
    )

    await callback.answer()