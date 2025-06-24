from pymongo import MongoClient
from config import MONGO_DB_URI

client = MongoClient(MONGO_DB_URI)
db = client["autofilter"]
collection = db["files"]

async def search_file(bot, message):
    query = message.text.strip().lower()
    results = collection.find({"title": {"$regex": query, "$options": "i"}})

    text = ""
    for r in results:
        text += f"📁 {r['title']}\n🔗 {r['link']}\n\n"

    if text:
        await message.reply(text)
    else:
        await message.reply("😔 Koi result nahi mila.")
