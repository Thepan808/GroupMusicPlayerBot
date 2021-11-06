import requests
from pyrogram import Client as Bot

from callsmusic import run
from config import API_HASH, API_ID, BOT_TOKEN
from handlers import __version__

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
)

print(f"[INFO]: GRAVE SAD v{__version__} STARTED !")

bot.start()
run()
