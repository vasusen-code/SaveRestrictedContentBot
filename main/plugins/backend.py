#Github.com/Vasusen-code

from main.plugins.helpers import get_link
from .. import API_ID, BOT_TOKEN, API_HASH, SESSION
from pyrogram import Client, filters
import re

Bot = Client(
    "Simple-Pyrogram-Bot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID
)

async def get_msg(userbot, client, sender, msg_link):
    chat = msg_link.split("/")[-2]
    msg_id = int(msg_link.split("/")[-1])
    if 't.me/c' in msg_link:
        msg = await userbot.copy_message("me", chat, msg_id)
        await client.send_message(int(sender), msg) 
    else:
        await client.copy_message(int(sender), chat, msg_id)
    
@Bot.on_message(filters.private)
async def start(bot, event):
    link = get_link(event.text)
    if not link:
        return
    if 't.me/+' in link:
        return
    if 't.me' in link:
        try:
            await get_msg(userbot, bot, event.chat.id, link)
        except Exception as e:
            return await event.reply(f'Error: `{str(e)}`')

Bot.run()
userbot.run()
