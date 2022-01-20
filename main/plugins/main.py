# Github.com/Vasusen-code

from main.plugins.helpers import start_userbot, get_link, forcesub, forcesub_text, join
from .. import API_ID, BOT_TOKEN, API_HASH, SESSION

from pyrogram import Client, filters

import re
import asyncio
    
Bot = Client(
    "Simple-Pyrogram-Bot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)
    
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
    if event.text == '/start':
        await event.reply_text(text="Send me Link of any message to clone it here.\n\nFor private channel message, send invite link first.")
    link = get_link(event.text)
    if not link:
        return
    xx = await forcesub(bot, event.chat.id)
    if xx is True:
        await event.reply_text(text=forcesub_text)
        return
    await start_userbot(userbot)
    if 't.me/+' in link:
        await event.reply_text(text=xy)
        return 
    if 't.me' in link:
        try:
            await get_msg(userbot, bot, event.chat.id, link)
        except Exception as e:
            if 'PEER_ID_INVALID' in str(e):
                return await event.reply_text(text='Channel not joined, Send invite link.')
            else:
                return await event.reply_text(text=f'Error: `{str(e)}`')

Bot.run()
userbot.start()
