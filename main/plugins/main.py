#Github.com/Vasusen-code

import time, os

from .. import bot as Drone
from .. import userbot

from telethon import events
from telethon.tl.types import DocumentAttributeVideo

from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload, fast_download

from main.plugins.pyroplug import Bot as pyrClient
from main.plugins.helpers import get_link, join, screenshot

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    edit = await event.reply('Trying to process.')
    if 't.me/+' in link:
        x, y = await join(userbot, link)
        await edit.edit(y)
        return 
    if 't.me' in link:
        if not 't.me/c/' in link:
            try:
                await copy_message(pyrClient, event.sender_id, link) 
                await edit.delete()
            except ValueError:
                await edit.edit("Send me only message link or Invite of private channel.")
            except Exception as e:
                if 'username' in str(e):
                    await edit.edit("Couldn't clone message, maybe i am banned from the given chat.")
                else:
                    await edit.edit(str(e))
        if 't.me/c/' in link:
             try:
                 chat =  int(msg_link.split("/")[-2])
                 msg_id = int(msg_link.split("/")[-1])
                 await edit.edit("Trying to Process.")
                 file = await userbot.get_messages(chat, ids=msg_id)
                 if not file:
                     await edit.edit("Couldn't get message!")
                 if file and file.text and not file.media:
                     await edit.edit(file.text)
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
                 if 'mp4' in name:
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
                 else:
                     caption = name
                     if file.text:
                         caption=file.text
                     thumb=None
                     if os.path.exists(f'{event.sender}.jpg'):
                         thumb = f'{event.sender}.jpg'
                     uploader = await fast_upload(name, name, time.time(), event.client, edit, '**UPLOADING:**')
                     await event.client.send_file(event.chat_id, uploader, caption=caption, thumb=thumb, force_document=True)
                     await edit.delete()
             except Exception as e:
                 print(e)
                 await edit.edit("Failed, try again!")
                     
                                
                                
                                
                                
