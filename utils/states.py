from aiogram.fsm.state import StatesGroup, State

class Payment(StatesGroup):
    waiting_for_amount = State()
    waiting_for_photo = State()