import json

DATABASE_PATH = "core/db.json"

def get_user(telegram_id):
    
    with open (DATABASE_PATH, "r", encoding="utf-8") as file:
        database = json.load(file)
        
    
    for user_id, user_data in database["users"].items():
        
        if user_data["telegram_id"] == telegram_id:
            return user_id, user_data
        
    
    return None, None