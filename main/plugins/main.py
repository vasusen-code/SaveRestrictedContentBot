#Github.com/Vasusen-code

import time, os

from .. import bot as Drone
from .. import userbot
from .. import FORCESUB as fs

from telethon import events
from telethon.tl.types import DocumentAttributeVideo

from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload, fast_download, force_sub

from main.plugins.helpers import get_link, join, screenshot

ft = f"To use this bot you've to join @{fs}."

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s == True:
        await event.reply(r)
        return
    edit = await event.reply('Trying to process.')
    if 't.me/+' in link:
        x, y = await join(userbot, link)
        await edit.edit(y)
        return 
    if 't.me' in link:
        if not 't.me/c/' in link:
            chat =  link.split("/")[-2]
            msg_id = link.split("/")[-1]
            await edit.edit(f'cloning {chat}-{msg_id}')
        if 't.me/c/' in link:
             try:
                 chat =  int('-100' + str(link.split("/")[-2]))
                 msg_id = int(link.split("/")[-1])
                 file = await userbot.get_messages(chat, ids=msg_id)
                 if not file:
                     await edit.edit("Couldn't get message!")
                     return
                 if file and file.text:
                     try:
                         if msg.text and not msg.media:
                             await event.client.send_message(event.chat_id, msg.text)
                         if msg.media.webpage:
                             await event.client.send_message(event.chat_id, msg.text)
                     except Exception:
                         pass
                 name = file.file.name
                 if not name:
                     if not file.file.mime_type:
                         await edit.edit("Couldn't fetch Name/Mime for the file.")
                         return
                     else:
                         if 'mp4' or 'x-matroska' in file.file.mime_type:
                             name = f'{chat}' + '-' + f'{msg_id}' + '.mp4'
                 await fast_download(name, file.document, userbot, edit, time.time(), '**DOWNLOADING:**')
                 await edit.edit("Preparing to upload.")
                 if 'mp4' in file.file.mime_type:
                     metadata = video_metadata(name)
                     height = metadata["height"]
                     width = metadata["width"]
                     duration = metadata["duration"]
                     attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
                     thumb = await screenshot(name, duration/2, event.sender_id)
                     caption = name
                     if file.text:
                         caption=file.text
                     uploader = await fast_upload(name, name, time.time(), event.client, edit, '**UPLOADING:**')
                     await event.client.send_file(event.chat_id, uploader, caption=caption, thumb=thumb, attributes=attributes, force_document=False)
                     await edit.delete()
                     os.remove(name)
                 elif 'x-matroska' in file.file.mime_type:
                     metadata = video_metadata(name)
                     height = metadata["height"]
                     width = metadata["width"]
                     duration = metadata["duration"]
                     attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
                     thumb = await screenshot(name, duration/2, event.sender_id)
                     caption = name
                     if file.text:
                         caption=file.text
                     uploader = await fast_upload(name, name, time.time(), event.client, edit, '**UPLOADING:**')
                     await event.client.send_file(event.chat_id, uploader, caption=caption, thumb=thumb, attributes=attributes, force_document=False)
                     await edit.delete()
                     os.remove(name)
                 else:
                     caption = name
                     if file.text:
                         caption=file.text
                     thumb=None
                     if os.path.exists(f'{event.sender_id}.jpg'):
                         thumb = f'{event.sender_id}.jpg'
                     uploader = await fast_upload(name, name, time.time(), event.client, edit, '**UPLOADING:**')
                     await event.client.send_file(event.chat_id, uploader, caption=caption, thumb=thumb, force_document=True)
                     await edit.delete()
                     os.remove(name)
             except Exception as e:
                 print(e)
                 if 'Peer'in str(e):
                     await edit.edit("Channel not found, have you joined it?")
                     return
                 await edit.edit("Failed, try again!")
                     
                                
                                
                                
                                
