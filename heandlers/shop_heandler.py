from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.shop_kb import get_products_kb
from keyboards.buy_kb import buy_kb

from data.get_user import get_user
from data.buy_product import buy_product

import json


router = Router()


PRODUCTS_PATH = "core/data/products.json"


def load_products():

    with open(
        PRODUCTS_PATH,
        encoding="utf-8"
    ) as file:

        return json.load(file)



async def edit_message(
    callback: CallbackQuery,
    text: str,
    keyboard=None
):

    if callback.message.photo:

        await callback.message.edit_caption(
            caption=text,
            reply_markup=keyboard
        )

    else:

        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard
        )



# =========================
# КАТАЛОГ
# =========================

@router.callback_query(F.data == "catalog")
async def catalog(callback: CallbackQuery):

    await edit_message(
        callback,
        "🛒 Каталог услуг:",
        get_products_kb()
    )

    await callback.answer()



# =========================
# ПРОСМОТР ТОВАРА
# =========================

@router.callback_query(F.data.startswith("product:"))
async def product(callback: CallbackQuery):

    product_id = callback.data.split(":")[1]


    products = load_products()


    if product_id not in products["products"]:

        await callback.answer(
            "❌ Товар не найден",
            show_alert=True
        )

        return


    product = products["products"][product_id]


    text = (
        f"📦 {product['name']}\n\n"
        f"{product['description']}\n\n"
        f"💰 Цена: {product['price']}₽"
    )


    await edit_message(
        callback,
        text,
        buy_kb(product_id)
    )


    await callback.answer()



# =========================
# ПОКУПКА
# =========================

@router.callback_query(F.data.startswith("buy:"))
async def buy(callback: CallbackQuery):

    product_id = callback.data.split(":")[1]


    products = load_products()


    if product_id not in products["products"]:

        await callback.answer(
            "❌ Товар не найден",
            show_alert=True
        )

        return



    product = products["products"][product_id]


    local_id, user = get_user(
        callback.from_user.id
    )


    if not user:

        await callback.answer(
            "❌ Пользователь не найден",
            show_alert=True
        )

        return



    price = product["price"]



    if user["balance"] < price:

        await callback.answer(
            "❌ Недостаточно средств",
            show_alert=True
        )

        return



    success = buy_product(
        local_id,
        product
    )



    if success:


        await edit_message(
            callback,
            (
                "✅ Покупка успешно оформлена!\n\n"
                f"📦 Товар: {product['name']}\n"
                f"💰 Списано: {price}₽\n\n"
                "⏳ Пишите админу в лс @JustF12 / @donke001"
            )
        )


    else:

        await callback.answer(
            "❌ Ошибка покупки",
            show_alert=True
        )

        return



    await callback.answer()