#Tg:MaheshChauhan/DroneBots
#Github.com/Vasusen-code

import time, os

from .. import bot as Drone
from .. import userbot, AUTH
from .. import FORCESUB as fs

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload, fast_download, force_sub

from main.plugins.helpers import get_link, screenshot

ft = f"To use this bot you've to join @{fs}."

async def get_pvt_content(event, chat, id):
    msg = await userbot.get_messages(chat, ids=id)
    await event.client.send_message(event.chat_id, msg) 
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def batch(event):
    if not event.is_private:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    if s == True:
        await event.reply(r)
        return       
    async with Drone.conversation(event.chat_id) as conv: 
        if s != True:
            await conv.send_message("Send me the message link you want to start saving from, as a reply to this message.", buttons=Button.force_reply())
            try:
                link = await conv.get_reply()
            except Exception as e:
                print(e)
                return await conv.send_message("Cannot wait more longer for your response!")
            if not 't.me/c/' in link.text:
                return await conv.send_message("Batch supported only for private restricted channels only!")
            try:
                _link = get_link(link.text)
                chat = int('-100' + (str(_link)).split("/")[-2])
                id = int((str(_link)).split("/")[-1])
            except Exception as e:
                print(e)
                return await conv.send_message("**Invalid link!**")
            await conv.send_message("Send me the number of files/range you want to save after the given message, as a reply to this message.", buttons=Button.force_reply())
            try:
                _range = await conv.get_reply()
            except Exception as e:
                print(e)
                return await conv.send_message("Cannot wait more longer for your response!")
            try:
                value = int(_range.text)
                if value > 100:
                    return await conv.send_message("You can only get 100 files in a single batch.")
            except ValueError:
                return await conv.send_message("Range must be an integer!")
            try:
                await userbot.get_messages(chat, ids=id)
            except Exception as e:
                print(e)
                return await conv.send_message("Have you joined the channel?")
            try:
                await private_batch(event, chat, id, value) 
                conv.cancel()
            except Exception as e:
                print(e)
                pass
            
async def private_batch(event, chat, offset, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        try:
            try:
                await get_pvt_content(event, chat, int(offset + i)) 
            except Exception:
                await get_res_content(event, chat, int(offset + i)) 
        except errors.FloodWaitError as fw:
            await asyncio.sleep(fw.seconds + 10)
            try:
                await get_pvt_content(event, chat, int(offset + i)) 
            except Exception:
                await get_res_content(event, chat, int(offset + i)) 
        protection = await event.client.send_message(event.chat_id, f"Sleeping for `{timer}` seconds to avoid Floodwaits and Protect account!")
        time.sleep(timer)
        await protection.delete()
            
async def get_res_content(event, chat, id):
    msg = await userbot.get_messages(chat, ids=id)
    if msg is None:
        await event.client.send_message(event.chat_id, f"Couldn't get this message:\n\nchannel:` {chat}`\nid: `{id}`")
        return
    try:
        if msg.text and not msg.media:
            await event.client.send_message(event.chat_id, msg.text)
        if msg.media.webpage:
            await event.client.send_message(event.chat_id, msg.text)
    except Exception:
        pass
    name = msg.file.name
    if not name:
        if not msg.file.mime_type:
            await event.client.send_message(event.chat_id, f"Couldn't get this message:\n\nchannel:` {chat}`\nid: `{id}`")
            return
        else:
            if 'mp4' or 'x-matroska' in msg.file.mime_type:
                name = f'{chat}' + '-' + f'{id}' + '.mp4'
    edit = await event.client.send_message(event.chat_id, "Preparing to Download!")
    await fast_download(name, msg.document, userbot, edit, time.time(), '**DOWNLOADING:**')
    await edit.edit("Preparing to upload.")
    if 'mp4' in msg.file.mime_type or 'x-matroska' in msg.file.mime_type:
        metadata = video_metadata(name)
        height = metadata["height"]
        width = metadata["width"]
        duration = metadata["duration"]
        attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
        thumb = await screenshot(name, duration/2, event.sender_id)
        caption = name
        if msg.text:
            caption=msg.text
        uploader = await fast_upload(name, name, time.time(), event.client, edit, '**UPLOADING:**')
        await event.client.send_file(event.chat_id, uploader, caption=caption, thumb=thumb, attributes=attributes, force_document=False)
        await edit.delete()
        os.remove(name)
    else:
        caption = name
        if msg.text:
            caption=msg.text
        thumb=None
        if os.path.exists(f'{event.sender_id}.jpg'):
            thumb = f'{event.sender_id}.jpg'
        uploader = await fast_upload(name, name, time.time(), event.client, edit, '**UPLOADING:**')
        await event.client.send_file(event.chat_id, uploader, caption=caption, thumb=thumb, force_document=True)
        await edit.delete()
        os.remove(name)
        
