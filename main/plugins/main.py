# Github.com/Vasusen-code

from main.plugins.helpers import get_link, join, screenshot
from main.plugins.display_progress import progress_for_pyrogram

from decouple import config

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None) #pyro session

from pyrogram.errors import FloodWait, BadRequest
from pyrogram import Client, filters
from ethon.pyfunc import video_metadata

import re, time, asyncio, logging, os

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

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
  
def thumbnail(sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    else:
         return None
      
async def get_msg(userbot, client, sender, msg_link, edit):
    chat = ""
    msg_id = int(msg_link.split("/")[-1])
    if 't.me/c/' in msg_link:
        chat = int('-100' + str(msg_link.split("/")[-2]))
        try:
            msg = await userbot.get_messages(chat, msg_id)
            file = await userbot.download_media(
                msg,
                progress=progress_for_pyrogram,
                progress_args=(
                    userbot,
                    "**DOWNLOADING:**\n",
                    edit,
                    time.time()
                )
            )
            await edit.edit('Trying to Upload.')
            caption = ""
            if msg.text is not None:
                caption = msg.text
            if str(file).split(".")[-1] == 'mkv' or 'mp4' or 'webm':
                if str(file).split(".")[-1] == 'webm' or 'mkv':
                    path = str(file).split(".")[0] + ".mp4"
                    os.rename(file, path) 
                    file = str(file).split(".")[0] + ".mp4"
                data = video_metadata(file)
                duration = data["duration"]
                thumb_path = await screenshot(file, duration/2, sender)
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
                thumb_path=thumbnail(sender)
                await client.send_document(
                    sender,
                    file, 
                    caption=caption,
                    thumb=thumb_path,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        client,
                        '**UPLOADING:**\n',
                        edit,
                        time.time()
                    )
                )
            await edit.delete()
        except Exception as e:
            await edit.edit(f'ERROR: {str(e)}')
            return 
    else:
        chat =  msg_link.split("/")[-2]
        await client.copy_message(int(sender), chat, msg_id)
        await edit.delete()
        
@Bot.on_message(filters.private & filters.incoming)
async def clone(bot, event):
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    edit = await bot.send_message(event.chat.id, 'Trying to process.')
    if 't.me/+' in link:
        xy = await join(userbot, link)
        await edit.edit(xy)
        return 
    if 't.me' in link:
        try:
            await get_msg(userbot, bot, event.chat.id, link, edit) 
        except FloodWait:
            return await edit.edit('Too many requests, try again later.')
        except ValueError:
            return await edit.edit('Send Only message link or Private channel invites.')
        except Exception as e:
            return await edit.edit(f'Error: `{str(e)}`')         
          
