from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_admin_pay_kb(user_id, amount):

    keyboard = InlineKeyboardBuilder()


    keyboard.button(
        text="✅ Одобрить",
        callback_data=f"accept_pay:{user_id}:{amount}"
    )


    keyboard.button(
        text="❌ Отклонить",
        callback_data=f"decline_pay:{user_id}:{amount}",
    )


    keyboard.adjust(2)


    return keyboard.as_markup()