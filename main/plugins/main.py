# Github.com/Vasusen-code

from main.plugins.helpers import start_userbot, get_link, forcesub, forcesub_text, join, set_timer, check_timer, screenshot
from main.plugins.display_progress import progress_for_pyrogram
from .. import API_ID, BOT_TOKEN, API_HASH, SESSION

from pyrogram import Client, filters
from ethon.pyfunc import video_metadata

import re
import time
import asyncio
    
process=[]
timer=[]

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
    chat = ""
    msg_id = int(msg_link.split("/")[-1])
    if 't.me/c' in msg_link:
        st, r = check_timer(sender, process, timer) 
        if st == False:
            await client.send_message(sender, r) 
        chat = int('-100' + str(msg_link.split("/")[-2]))
        try:
            msg = await userbot.get_messages(chat, msg_id)
            edit = await client.send_message(sender, 'Trying to process.')
            file = await userbot.download_media(
                msg,
                progress=progress_for_pyrogram,
                progress_args=(
                    userbot,
                    "**DOWNOOADING:**\n",
                    edit,
                    time.time()
                )
            )
            await edit.edit('Trying to Upload.')
            caption = ""
            if msg.text is not None:
                caption = msg.text
            if str(file).split(".")[-1] == 'mp4':
                data = video_metadata(file)
                duration = data["duration"]
                thumb_path = screenshot(file, duration/2)
                await client.send_video(
                    chat_id=sender,
                    video=file,
                    caption=caption,
                    supports_streaming=True,
                    duration=duration,
                    thumb=thumb_path,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        client,
                        '**UPLOADING:**\n',
                        edit,
                        time.time()
                    )
                )
            else:
                await client.send_document(
                    sender,
                    file, 
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        client,
                        '**UPLOADING:**\n',
                        edit,
                        time.time()
                    )
                )
            await edit.delete()
            await set_timer(client, sender, process, timer) 
        except Exception as e:
            await edit.edit(str(e))
    else:
        chat =  msg_link.split("/")[-2]
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
    try:
        await start_userbot(userbot)
    except Exception as e:
        if 'Client is already connected' in str(e):
            pass
        else:
            return
    if 't.me/+' in link:
        xy = await join(userbot, link)
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
