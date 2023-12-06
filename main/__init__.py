#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29098616
API_HASH = "635f6ec82aa166be7682113b562e0898"
BOT_TOKEN = "6885013483:AAGtgv-j1-fUz-ri-_kTdJtr9_0LnTm17U8"
SESSION = "BQBYYfd2YSYMtiUyWz0QyOMuQbgEXNijyNRAh0hW1_snYqzA3XgLO1UgT8f9CKad3dP4Myi2D5fCEe98He9uOd6v9VTjXYV-vZU0ghVyWRJKLPu0sQaeZGpcAh2WcTGZ_UzGIyCeH6FnnSI6u5PjXbJPEuZQZvXdErmvnDuqktjlkvTcQ6orJoy7pCFcxUqTJ0YHYXJLTCXPruYIE1V3cSOj9O-FFbex4jsl9X79Ic69PUlkierdOW5lZ-k6wH7wD-i48XVj1mAK6zai6oWWNe4CTHT0fAjFfLkmDmFYF-mdq9VuQcA5SAt3ROWz8VLs4DppFO5TnQMCEv_WyHwa4iaiAAAAAVs7moUA"
FORCESUB = "mychannel124588"
AUTH = 5825600133

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
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
python3 -m main
