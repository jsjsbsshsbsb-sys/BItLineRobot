from aiogram.utils.keyboard import InlineKeyboardBuilder
from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
CATALOG_PATH = BASE_DIR / "data" / "products.json"


def get_products_kb():

    with open(
        CATALOG_PATH,
        encoding="utf-8"
    ) as file:
        data = json.load(file)


    kb = InlineKeyboardBuilder()


    for product_id, product in data["products"].items():

        kb.button(
            text=f"{product['name']} — {product['price']}₽",
            callback_data=f"product:{product_id}"
        )


    kb.button(
        text="⬅️ Назад",
        callback_data="back"
    )


    kb.adjust(1)

    return kb.as_markup()