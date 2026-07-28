import json


def buy_product(local_id, price):

    with open(
        "db.json",
        encoding="utf-8"
    ) as file:
        db=json.load(file)


    user=db["users"].get(str(local_id))


    if not user:
        return False, "Пользователь не найден"


    if user["balance"] < price:
        return False, "Недостаточно средств"


    user["balance"] -= price


    with open(
        "core/db.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            db,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True, user["balance"]
