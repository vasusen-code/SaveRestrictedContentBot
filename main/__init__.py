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
SESSION = config("AQBRw-dE78lETUCaaas9EVqziF6mIpY5QNdTp07gON68D3lbGHGpOWRs8MKZ0WUUlnUnjIUCF2OlJquemJ-5EZEsSs8A_XRzVSd7NmlSplAkxWqmG3oR6CXT8-RGqbBStHo3U6uI16fDT7p7l0vGPyNPqzyJAInnrVTh96k4drWDpRfsTrFNFPTEgmswnp6UNo2gvPilBHoxtA47xYx04cvZLxZ3NgrqUHtxfdipNzWlx3Q5_M5H_9SRe9rwPZw4_JbRm9muAT4dZd0_YoAUBJx_tzI85XUJpX2ylchEQsZ28-y2vpnPhvqlBrMEQ2ZmSn-CC8dJ6TcN0R6BCK6c5DqQea_PMQA", default=None)
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
