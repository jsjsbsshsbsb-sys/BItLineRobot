from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.back_kb import create_back_kb
from data.update_balance import update_balance
from data.add_payment_history import add_payment_history
from data.get_user_by_local_id import get_user_by_local_id


router = Router()


@router.callback_query(F.data.startswith("accept_pay:"))
async def accept_pay(callback: CallbackQuery):

    _, user_id, amount = callback.data.split(":")

    amount = int(amount)


    # Пополняем баланс
    success = update_balance(
        user_id,
        amount
    )


    if not success:
        await callback.answer(
            "❌ Пользователь не найден",
            show_alert=True
        )
        return


    # Добавляем запись в историю платежей
    history_added = add_payment_history(
        user_id,
        amount,
        "Одобрено"
    )


    if not history_added:
        await callback.answer(
            "⚠️ Баланс изменён, но история не сохранилась",
            show_alert=True
        )


    # Получаем обновлённые данные
    _, user = get_user_by_local_id(
        user_id
    )


    if user:

        telegram_id = user["telegram_id"]

        await callback.bot.send_message(
            chat_id=telegram_id,
            text=(
                "✅ Ваш платёж подтверждён!\n\n"
                f"💰 Пополнено: {amount} ₽\n"
                f"💵 Баланс: {user['balance']} ₽"
            ),
            reply_markup=create_back_kb()
        )


    # Убираем кнопки у админа
    await callback.message.edit_reply_markup(
        reply_markup=None
    )


    await callback.message.answer(
        f"✅ Пользователю {user_id} начислено {amount} ₽"
    )


    await callback.answer(
        "Баланс обновлён"
    )


@router.callback_query(F.data.startswith("decline_pay:"))
async def decline_pay(callback: CallbackQuery):

    _, user_id, amount = callback.data.split(":")

    amount = int(amount)


    history_added = add_payment_history(
        user_id,
        amount,
        "Отклонено"
    )


    if not history_added:
        await callback.answer(
            "❌ Пользователь не найден",
            show_alert=True
        )
        return


    _, user = get_user_by_local_id(user_id)


    if user:

        await callback.bot.send_message(
            chat_id=user["telegram_id"],
            text=(
                "❌ Ваш платёж был отклонён администрацией.\n\n"
                f"💰 Сумма: {amount} ₽"
            ),
            reply_markup=create_back_kb()
        )


    await callback.message.edit_reply_markup(
        reply_markup=None
    )


    await callback.message.answer(
        f"❌ Заявка пользователя {user_id} отклонена."
    )


    await callback.answer(
        "Платёж отклонён"
    )