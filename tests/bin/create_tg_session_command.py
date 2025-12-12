from dotenv import dotenv_values
from pyrogram import Client

env = dotenv_values("back/secrets/.env")
api_id = env["TG_API_ID"]
api_hash = env["TG_API_HASH"]

app = Client('/tmp/session', api_id=api_id, api_hash=api_hash)

app.start()
session = app.export_session_string()
app.stop()

print(f'API ID: {api_id}')
print(f'API HASH: {api_hash}')
print(f'SESSION: {session}')