from pymongo import MongoClient
from config import MONGO_DB_URI

client = MongoClient(MONGO_DB_URI)
db = client["autofilter"]
collection = db["files"]

async def save_file(bot, message):
    if not message.caption:
        return

    title = message.caption.strip()
    link = f"https://t.me/{message.chat.username}/{message.message_id}"

    if collection.find_one({"link": link}):
        return

    collection.insert_one({
        "title": title,
        "link": link
    })
