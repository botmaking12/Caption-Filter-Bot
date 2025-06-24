from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from uploader import save_file
from filter import search_file

app = Client("CaptionBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.channel & (filters.document | filters.video))
async def on_file_upload(client, message):
    await save_file(client, message)

@app.on_message(filters.private | filters.group)
async def on_user_query(client, message):
    await search_file(client, message)

app.run()
