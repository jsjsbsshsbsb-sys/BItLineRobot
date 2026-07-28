import json
from datetime import datetime


DATABASE_PATH = "db.json"


def add_payment_history(
    user_id,
    amount,
    status="Одобрено"
):

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        database = json.load(file)


    user_id = str(user_id)


    if user_id not in database["users"]:
        return False


    history = database["users"][user_id]["payments_history"]


    payment_id = str(len(history) + 1)


    history[payment_id] = {
        "amount": amount,
        "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "type": "Пополнение",
        "status": status
    }


    with open(DATABASE_PATH, "w", encoding="utf-8") as file:
        json.dump(
            database,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True
