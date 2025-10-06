from dotenv import load_dotenv
import os
from pyrogram import Client

load_dotenv()
api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")
print(api_id)
print(api_hash)
with Client("/Users/acrosspaper/code/vacancy/vacancy_back/secrets/my_account.session", api_id=api_id, api_hash=api_hash) as app:
    print(app.export_session_string())