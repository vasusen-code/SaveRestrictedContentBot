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
      
async def check(userbot, client, link):
    msg_id = int(link.split("/")[-1])
    if 't.me/c/' in link:
        try:
            chat = int('-100' + str(link.split("/")[-2]))
            await userbot.get_messages(chat, msg_id)
            return True, None
        except ValueError:
            return False, "**Invalid Link!**"
        except Exception:
            return False, "Have you joined the channel?"
    else:
        try:
            chat = str(link.split("/")[-2])
            await client.get_messages(chat, msg_id)
            return True, None
        except Exception:
            return False, "Maybe bot is banned from the chat, or your link is invalid!"
            
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
                    edit = await client.edit_message_text(sender, edit_id, "Cloning.")
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete()
                    return
            if not msg.media:
                if msg.text:
                    edit = await client.edit_message_text(sender, edit_id, "Cloning.")
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete()
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
            caption = str(file)
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
            elif str(file).split(".")[-1] == 'jpg' or 'jpeg' or 'png':
                await client.send_photo(
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
        edit = await client.edit_message_text(sender, edit_id, "Cloning.")
        chat =  msg_link.split("/")[-2]
        try:
            await client.copy_message(int(sender), chat, msg_id)
        except Exception as e:
            print(e)
        await edit.delete()
        
async def get_bulk_msg(userbot, client, sender, msg_link, _range):
    edit = await client.send_message(sender, 'Processing!')
    edit_id = edit.message_id
    chat = ""
    msg_id = int(msg_link.split("/")[-1] + str(_range))
    if 't.me/c/' in msg_link:
        _chat = int(msg_link.split("/")[-2])
        chat = int('-100' + str(msg_link.split("/")[-2]))
        try:
            msg = await userbot.get_messages(chat, msg_id)
            if not msg.media:
                if msg.text:
                    edit = await client.edit_message_text(sender, edit_id, "Cloning.")
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete()
                    return
            if msg.media:
                if 'web_page' in msg.media:
                    edit = await client.edit_message_text(sender, edit_id, "Cloning.")
                    await client.send_message(sender, msg.text.markdown)
                    await edit.delete()
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
            caption = str(file)
            if msg.caption is not None:
                caption = msg.caption
            if str(file).split(".")[-1] == 'mkv' or 'mp4':
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
            elif str(file).split(".")[-1] == 'jpg' or 'jpeg' or 'png':
                await client.send_photo(
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
            print(e)
            await client.send_message(sender, f"Couldn't get this message: `t.me/c/{_chat}/{msg_id}`")
            return 
    else:
        edit = await client.edit_message_text(sender, edit_id, "Cloning.")
        chat =  msg_link.split("/")[-2]
        try:
            await client.copy_message(int(sender), chat, msg_id)
        except Exception as e:
            print(e)
            return await client.send_message(sender, f"Couldn't get this message: `t.me/{chat}/{msg_id}`")
        await edit.delete()
        
