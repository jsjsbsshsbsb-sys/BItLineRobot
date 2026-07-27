from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_menu():

    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="Наш канал",
        url="https://t.me/BitLineOfficial"
    )

    keyboard.button(
        text="Отзывы",
        url="https://t.me/+oCUN-k97zkVhZTM6"
    )

    keyboard.button(
        text="👤 Профиль",
        callback_data="profile"
    )

    keyboard.button(
        text="🛒 Магазин",
        callback_data="catalog"
    )

    keyboard.button(
        text="📜 История покупок",
        callback_data="payments_history"
    )

    keyboard.button(
        text="💰 Пополнить",
        callback_data="pay"
    )

    keyboard.button(
        text="🆘 Поддержка",
        url="https://t.me/JustF12"
    )

    keyboard.adjust(2)

    return keyboard.as_markup()