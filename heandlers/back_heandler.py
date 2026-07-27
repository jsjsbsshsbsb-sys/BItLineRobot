from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.menu import create_menu


router = Router()


@router.callback_query(F.data.in_({"back"}))
async def back_to_menu(callback: CallbackQuery):

    message = callback.message

    if message.photo:

        await message.edit_caption(
            caption="🏠 Главное меню",
            reply_markup=create_menu()
        )

    else:

        await message.edit_text(
            "🏠 Главное меню",
            reply_markup=create_menu()
        )

    await callback.answer()