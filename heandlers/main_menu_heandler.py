from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.menu import create_menu


router = Router()


@router.callback_query(F.data == "main_menu")
async def main_menu(callback: CallbackQuery):

    text = "🏠 Главное меню"


    if callback.message.photo:

        await callback.message.edit_caption(
            caption=text,
            reply_markup=create_menu()
        )

    else:

        await callback.message.edit_text(
            text=text,
            reply_markup=create_menu()
        )


    await callback.answer()