#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("16191861", default=None, cast=int)
API_HASH = config("8afcd0285c66c4d12c6199ba78309636", default=None)
BOT_TOKEN = config("5517378684:AAHMe8LHS1lEoFoo16JMGmIFhf5aQFFlOV8", default=None)
SESSION = config("BQChAPUApZywJ_TPsoXKvgRriqcxBfY4p_5xO0kbrQ9vPci-H1u93ctxOy6jWP_b-0UUJbGCYhSbTkKJNvHGSco8mr3x3Z5STVE_BOeDR39Bwxl0HftWB88RUkGXF0ea_jsF-3vRUGnG0TNqdeWxemUXgtODFigxwofHLllZoq_oif_KYd2YDcPBTL3kv1fsCmnpLSRAOSEfaLrAEoju_7sBzod5NXo1NnVYcHRyXWVzv1ceoUMSUo22YmmHgsMZXv7a_XsbpfgxDwFVjvrOdp4aBEV7JmrlqQB7ZmdjKQlWLSDVYfEb9cp8UYTRElTVPobHWI9NdLQ8YJZSIVj1Sf20TZXAogAAAAB3pzF-AA", default=None)
FORCESUB = config("@jesnita_full_movie", default=None)
AUTH = config("2007445886", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
