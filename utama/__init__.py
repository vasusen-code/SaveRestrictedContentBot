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
SESSION = config("BQDBZ_TjTRPb7Y1RG8yojntSJlFSrc7weQMYRkutjLGxWawv8YwBxMZdyEYRL7dsamfbuBSIm5HsQgoBNHtgyHMwHqaN20KpMj_aoedvuRjOxEkyuDKagQ2_ra3ICUqFKvjw1YUYSq2SmvXNe18gjJJFoAYrWWsKyl09lPZNUlvzSnVFROek9LD6N5V0NcBqTvaVKEHUdvWIS9qq94VdXav3l2lla9M-BlZi2CGDogA0iSqFaswHmAOmwwKDnm-IZpfCMv3p5qCzgLVf10Gs5WDc70NvAh8Ug_-C6IEn82yM5xBh5YsXVflrcm4JTqZx4vGBQXq7O3Yr6W0qvDJSBDfdd6cxfgA", default=None)
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
