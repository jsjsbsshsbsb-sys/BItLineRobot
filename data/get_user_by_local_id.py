import json

DATABASE_PATH = "db.json"


def get_user_by_local_id(local_id):

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        database = json.load(file)


    local_id = str(local_id)


    if local_id in database["users"]:
        return local_id, database["users"][local_id]


    return None, None
