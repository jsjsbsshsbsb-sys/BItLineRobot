from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_back_kb(callback_data="back"):

    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="⬅️ Назад",
        callback_data=callback_data
    )

    return keyboard.as_markup()