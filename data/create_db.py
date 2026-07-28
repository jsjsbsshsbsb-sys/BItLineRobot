import json
import os


DATABASE_PATH = "db.json"


#Создание бд
def create_database():
    
    if not os.path.exists(DATABASE_PATH):
        database = {
            "users": {},
            "admins": {}
        }
        
        with open(DATABASE_PATH, "w", encoding="utf-8") as file:
            json.dump(database, file, ensure_ascii=False, indent=False)
        
        print("База данных создана!")
