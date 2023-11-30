#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 13999676
API_HASH = d707bccfa731029b8ca5bef0e5afd813
BOT_TOKEN = 6389857059:AAHJuopfnnNLRj8mZt9Bwjl_F1_bzRtUFwQ
SESSION = BQDVnjwATAKNMsPvTdCuocJUisfSoefTPHSV5-a0zVHyizBLOoRRGzJBhRrM2VhOkV_cTRv67mLo5ShiEEm4216beN8UQx5cPbHMafSt78syGy_p373KmCw8ASLuv1oaDc-cYc3UmwIeg8TKb4L9k4aKIeQmuZcumU1P6IYU8JG7tyS-KSCqtfYaQTYBRPHA_Qe0fbo1kXDhSMavGg3VgkPdIHvyNGTd0q4vWIcU_sOT6D4Iwkr9klfFVHJJ-gek6PrQkzGCkMxdkaauWQ5wsH3WgSc6gf1R5V5HzQSu8RWxgZpTas7zXMs-qAcrM6s0QrbJChAivldkNW6Ra6jVlWEdpMc25wAAAABLCzuiAA
FORCESUB = indomilkonlyfans

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
