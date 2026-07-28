import json
from datetime import datetime


DATABASE = "db.json"


def buy_product(local_id, product):

    with open(
        DATABASE,
        encoding="utf-8"
    ) as file:
        db = json.load(file)


    local_id = str(local_id)


    if local_id not in db["users"]:
        return False


    user = db["users"][local_id]


    price = product["price"]


    if user["balance"] < price:
        return False


    user["balance"] -= price


    if "purchases" not in user:
        user["purchases"] = {}


    purchase_id = str(
        len(user["purchases"]) + 1
    )


    user["purchases"][purchase_id] = {

        "product": product["name"],
        "price": price,
        "date": datetime.now().strftime(
            "%d.%m.%Y %H:%M"
        )

    }


    with open(
        DATABASE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            db,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True
