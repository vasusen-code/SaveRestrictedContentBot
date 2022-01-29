#Github.com/Vasusen-code

from .. import bot as Drone
from .. import userbot

from telethon import events

from ethon.pyfunc import video_metadata
from ethon.telefunc import fast_upload,fast_download

from main.plugins.pyroplug import Bot as pyrClient

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    edit = await event.reply(event.chat.id, 'Trying to process.')
    if 't.me/+' in link:
        xy = await join(userbot, link)
        await edit.edit(xy)
        return 
    if 't.me' in link:
        if not 't.me/c/' in link:
            try:
                await copy_message(pyrClient, link) 
            except ValueError:
                await edit.edit("Send me only message link or Invite of private channel.")
            except Exception:
                await edit.edit("Couldn't clone message, maybe i am banned from the given chat.")
        if 't.me/c/' in link:
             try:
                 chat =  int(msg_link.split("/")[-2])
                 msg_id = int(msg_link.split("/")[-1])
                 await event.
