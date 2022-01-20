# Github.com/Vasusen-code

from main.plugins.helpers import get_link, forcesub_text
from .. import API_ID, BOT_TOKEN, API_HASH, SESSION

from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

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

async def forcesub(bot, sender):
    if FORCESUB is not None:
        try:
            user = await bot.get_chat_member(FORCESUB, sender)
            if user.status == "kicked":
                return True
        except UserNotParticipant:
            return True
            
async def get_msg(userbot, client, sender, msg_link):
    chat = msg_link.split("/")[-2]
    msg_id = int(msg_link.split("/")[-1])
    if 't.me/c' in msg_link:
        msg = await userbot.copy_message("me", chat, msg_id)
        await client.send_message(int(sender), msg) 
    else:
        await client.copy_message(int(sender), chat, msg_id)
    
@Bot.on_message(filters.private)
async def clone(bot, event):
    link = get_link(event.text)
    if not link:
        return
    xx = await forcesub(bot, event.chat.id)
    if xx is True:
        await event.reply_text(forcesub_text)
        return
    if 't.me/+' in link:
        return
    if 't.me' in link:
        try:
            await get_msg(userbot, bot, event.chat.id, link)
        except Exception as e:
            return await event.reply_text(f'Error: `{str(e)}`')

Bot.run()
userbot.run()
