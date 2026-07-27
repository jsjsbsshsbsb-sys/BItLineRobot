from aiogram import Dispatcher

from heandlers.start import router as start_router
from heandlers.profile_heandler import router as profile_router
from heandlers.pay_heandler import router as pay_router
from heandlers.back_heandler import router as back_router
from heandlers.check_heandler import router as check_router
from heandlers.history_heandler import router as history_router
from heandlers.main_menu_heandler import router as main_menu_router
from heandlers.shop_heandler import router as shop_router

def register_routers(dp: Dispatcher):
    
    dp.include_routers(start_router, profile_router,
                       pay_router, back_router,
                       check_router, history_router,
                       main_menu_router, shop_router)