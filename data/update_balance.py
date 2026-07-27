import json

DATABASE_PATH = "core/db.json"


def update_balance(local_id, amount):

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        database = json.load(file)


    local_id = str(local_id)


    if local_id not in database["users"]:
        return False


    database["users"][local_id]["balance"] += amount


    with open(DATABASE_PATH, "w", encoding="utf-8") as file:
        json.dump(
            database,
            file,
            indent=4,
            ensure_ascii=False
        )


    return True