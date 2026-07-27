from aiogram import Router
from aiogram import types
from aiogram.types import Message
from aiogram.filters import CommandStart


from data.create_db import create_database
from data.create_new_user import create_user
from keyboards.menu import create_menu


router = Router()

@router.message(CommandStart())
async def start(msg: Message):
    
    create_database()
    
    referrer = None

    user_id, registered = create_user(
        
        telegram_id = msg.from_user.id,
        first_name = msg.from_user.first_name,
        referrer=referrer
        
    )
    
    ref_link = f"https://t.me/BitLineRobot?start={user_id}"
    
    
    await msg.answer_photo(
        caption=f"Добро пожаловать {msg.from_user.first_name}!\n"
        f"ваш внутрений ID: <code> {user_id}</code>\n"
        f"Дата регистрации: {registered}\n\n",
        parse_mode="html",
        photo="AgACAgIAAxkBAAMCamH-NeYvGChnpiGa-Jlaq-aBrzMAArQVaxu2yBBL7MIHD8Tjnd4BAAMCAAN4AAM9BA",
        reply_markup=create_menu()
        )