from pyrogram import Client
import secrets.secrets as secrets

app = Client("secrets/my_account", api_id=secrets.tg_api_id, api_hash=secrets.tg_api_hash)
app.start()
app.stop()