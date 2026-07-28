import json
import random
from datetime import datetime

from data.db_manager import save_db

DATABASE_PATH = "db.json"

def create_user(telegram_id, first_name, referrer=None):
    
    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        database = json.load(file)
        
        
        #Проверка на наличие пользователя в БД
        for user_id, user_data in database["users"].items():
            
            if user_data["telegram_id"] == telegram_id:
                return user_id, database["users"][user_id]["registered"]
    
    #Создание айди
    while True:
        user_id = str(random.randint(100000, 999999))
        
        if user_id not in database["users"]:
            break
    
    database["users"][user_id] = {
        "telegram_id": telegram_id,
        "name": first_name,
        "registered": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "referrer": referrer,
        "referrals": [],
        "balance": 0,
        "payments_history": {}
    }
    
    # Добавляем нового пользователя в список приглашенных
    if referrer:

        if referrer in database["users"]:
            database["users"][referrer]["referrals"].append(user_id)
    
    save_db(
        database
    )
    
    return user_id, database["users"][user_id]["registered"]
