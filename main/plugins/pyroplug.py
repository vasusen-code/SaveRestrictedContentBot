# Github.com/Vasusen-code

import asyncio, time, os

from .. import Bot
from main.plugins.progress import progress_for_pyrogram
from main.plugins.helpers import screenshot

from pyrogram import Client, filters 
from ethon.pyfunc import video_metadata

def thumbnail(sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    else:
         return None
      
async def get_msg(userbot, client, sender, edit_id, msg_link):
    edit = ""
    chat = ""
    msg_id = int(msg_link.split("/")[-1])
    if 't.me/c/' in msg_link:
        chat = int('-100' + str(msg_link.split("/")[-2]))
        try:
            msg = await userbot.get_messages(chat, msg_id)
            if msg.media:
                if 'web_page' in msg.media:
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete(sender, edit_id)
                    return
            if not msg.media:
                if msg.text:
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete(sender, edit_id)
                    return
            edit = await client.edit_message_text(sender, edit_id, "Trying to Download.")
            file = await userbot.download_media(
                msg,
                progress=progress_for_pyrogram,
                progress_args=(
                    client,
                    "**DOWNLOADING:**\n",
                    edit,
                    time.time()
                )
            )
            await edit.edit('Prearing to Upload!')
            caption = ""
            if msg.caption is not None:
                caption = msg.caption
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
            if 'CHANNEL' in str(e).split("_") and 'INVALID' in str(e).split("_"):
                await client.edit_message_text(sender, edit_id, "Have you joined the channel?")
                return 
            await client.edit_message_text(sender, edit_id, f'ERROR: {str(e)}')
            return 
    else:
        edit = await client.edit_message_text(sender, "Cloning.")
        chat =  msg_link.split("/")[-2]
        await client.copy_message(int(sender), chat, msg_id)
        await edit.delete()
        
