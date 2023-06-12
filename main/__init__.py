#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", ="6722919", cast=int)
API_HASH = config("API_HASH", ="82d6d7b498bfba5ea9959deff02c8a4b")
BOT_TOKEN = config("BOT_TOKEN", ="5314869516:AAFcUf7Ga492e9PA88HIpspOs2RA0iiCGfA")
SESSION = config("SESSION", ="BQCJB5JBtRgD5EA54X4S3fYx8iLVOzQzflDBg_AWquCvwu3R4CWGGnz200NP7LJBHGV0uszePajc5GhOw1qhzqxT1lkBoHXedhagYK-JpXPXpXTZfRR0413xhpZfblJErm9FTi5cRpsxGEHigwFZlG_i9Wiw5cSaNlNfEW9gCRRgQjwDhtzJCm2K8AwH7q3RFjWnEMQZOKAyg0YdmtG1Brq1y2jGuB-DqOKUS6lJB5PVN5eEIr16I4AgnBGmDFVFu1imE3HX-1V4srcA9PsXAEzsSOmqdCunVEy9hWkKH4ImqzCy2oUOQ34ZHyuqyh75vWYvmU1r1pD49yBkahMzw7jpU1gxogA")
FORCESUB = config("FORCESUB", ="PrimeMovieCity")
AUTH = config("AUTH", ="1398288802", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
