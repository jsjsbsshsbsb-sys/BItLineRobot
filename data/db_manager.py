import json
import os


DATABASE_PATH = "db.json"

#Сохранение бд
def save_db(database):
    
    with open(DATABASE_PATH, "w", encoding="utf-8") as file:
        json.dump(
            database,
            file,
            ensure_ascii=False,
            indent=4
        )
