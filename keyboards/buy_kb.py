from aiogram.utils.keyboard import InlineKeyboardBuilder


def buy_kb(product_id):

    kb = InlineKeyboardBuilder()

    kb.button(
        text="💳 Купить",
        callback_data=f"buy:{product_id}"
    )

    kb.button(
        text="⬅️ Назад",
        callback_data="main_menu"
    )

    kb.adjust(1)

    return kb.as_markup()