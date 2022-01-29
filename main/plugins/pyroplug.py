# Github.com/Vasusen-code

from .. import API_ID, API_HASH, BOT_TOKEN
 
from pyrogram import Client

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

async def copy_message(client, sender, msg_link):
    chat =  msg_link.split("/")[-2]
    msg_id = msg_link.split("/")[-1]
    await client.copy_message(int(sender), chat, msg_id)
