#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession


from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29287695
API_HASH = fd378e3dd671ed4c83368f894090ba94
BOT_TOKEN = 6308831657:AAFfhx4BzcwOsw8nwlc6IPSP79vZqcPk_1Q
SESSION = BQG-5Q8AZzBR1faRMzt-gTaDi3v9qgVz42UCxzfMTBfj62CLkbfileXthWINCWXZl42UykNtdrVHyFqboPEJe3YCyRXMbWuGeKUoChryqrZ8m5SoM4eiQmuuLkcX0cm83NVZsTBPZuvISMfAfor5w6LyEBykHt8WpdSAKAe78YRcC0Wr0pYoc0rV6RGy2uKXRClK-fGeJk7o4p7aTdo0_t2nU0yBdwZF3_gdYa8UFFm-77gPTwKOAyST9Yt9Bagi9TyxlnHwsz6k77EGchkChW6L8hUu0UQxctYVS1-YQ1F4izk_ty5oU-kML8VPgx4nvYZdGYUsA1x2GUe_zw2AwEwf-r2oUAAAAABQFrewAA
FORCESUB = @Medico_helper_2 
AUTH = 1058482162

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
