from aiogram import Router, F
from aiogram.types import CallbackQuery

from data.get_user import get_user
from keyboards.back_kb import create_back_kb


router = Router()


@router.callback_query(F.data == "payments_history")
async def payments_history(callback: CallbackQuery):

    local_id, user = get_user(
        callback.from_user.id
    )


    if not user:

        await callback.answer(
            "❌ Пользователь не найден",
            show_alert=True
        )
        return



    history = user.get(
        "payments_history",
        {}
    )


    if not history:

        text = (
            "📜 История операций\n\n"
            "У вас пока нет операций."
        )

    else:

        text = (
            "📜 История операций:\n\n"
        )


        for payment_id, payment in history.items():

            text += (
                f"#{payment_id}\n"
                f"💰 Сумма: {payment['amount']} ₽\n"
                f"📅 Дата: {payment['date']}\n"
                f"📌 Тип: {payment['type']}\n"
                f"🔹 Статус: {payment['status']}\n\n"
            )


    # Проверяем, фото это или обычный текст
    if callback.message.photo:

        await callback.message.edit_caption(
            caption=text,
            reply_markup=create_back_kb()
        )

    else:

        await callback.message.edit_text(
            text=text,
            reply_markup=create_back_kb()
        )


    await callback.answer()