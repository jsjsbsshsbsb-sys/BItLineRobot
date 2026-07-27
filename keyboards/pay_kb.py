from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_pay_kb():
    
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(text="Оплатил", callback_data="paid", style="success")
    
    keyboard.adjust(1)
    
    return keyboard.as_markup()

def create_paid_kb():
    ...