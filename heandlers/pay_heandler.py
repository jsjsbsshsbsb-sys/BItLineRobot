from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards.back_kb import create_back_kb
from utils.states import Payment

from config import ADMIN_GROUP
from data.get_user import get_user

from keyboards.admin_pay_kb import create_admin_pay_kb


router = Router()


# Нажатие "Пополнить"
@router.callback_query(F.data == "pay")
async def pay(callback: CallbackQuery, state: FSMContext):

    await callback.message.edit_caption(
        caption="💰 Введите сумму пополнения:",
        reply_markup=create_back_kb()
    )

    await state.set_state(
        Payment.waiting_for_amount
    )

    await callback.answer()



# Получение суммы
@router.message(Payment.waiting_for_amount)
async def get_amount(message: Message, state: FSMContext):

    if not message.text or not message.text.isdigit():

        await message.answer(
            "❌ Введите сумму только цифрами."
        )
        return


    amount = int(message.text)


    if amount <= 0:

        await message.answer(
            "❌ Сумма должна быть больше нуля."
        )
        return


    await state.update_data(
        amount=amount
    )


    await message.answer(
        "📸 Теперь отправьте фотографию чека."
    )


    await state.set_state(
        Payment.waiting_for_photo
    )



# Получение чека
@router.message(Payment.waiting_for_photo, F.photo)
async def receive_photo(
    message: Message,
    state: FSMContext,
    bot: Bot
):

    photo = message.photo[-1].file_id


    data = await state.get_data()

    amount = data.get("amount", 0)



    local_id, user = get_user(
        message.from_user.id
    )


    if user:

        caption = (
            "💳 Новая заявка на пополнение\n\n"

            f"👤 Пользователь: {user['name']}\n"
            f"🆔 BitLine ID: <code>{local_id}</code>\n"
            f"📱 Telegram ID: <code>{user['telegram_id']}</code>\n\n"

            f"💰 Сумма: <b>{amount}</b> ₽\n"
            f"💵 Баланс: {user['balance']} ₽\n"
            f"📅 Регистрация: {user['registered']}"
        )

    else:

        caption = (
            "💳 Новая заявка на пополнение\n\n"

            f"👤 Имя: {message.from_user.full_name}\n"
            f"📱 Telegram ID: <code>{message.from_user.id}</code>\n\n"
            f"💰 Сумма: <b>{amount}</b> ₽"
        )


    await bot.send_photo(
        chat_id=ADMIN_GROUP,
        photo=photo,
        caption=caption,
        parse_mode="HTML",
        reply_markup=create_admin_pay_kb(
            local_id,
            amount
        )
    )


    await message.answer(
        "✅ Чек успешно отправлен администрации.\n"
        "Ожидайте проверки."
    )


    await state.clear()



# Если отправили не фото
@router.message(Payment.waiting_for_photo)
async def wrong_message(message: Message):

    await message.answer(
        "❌ Пожалуйста, отправьте фотографию чека."
    )