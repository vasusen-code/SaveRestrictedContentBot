import os

from ethon.mystarts import start_srb
from telethon import Button, events

from .. import AUTH
from .. import bot as Drone

S = "/" + "s" + "t" + "a" + "r" + "t"


@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def set_callback_handler(event):
    if event.sender_id in AUTH:
        Drone = event.client
        button = await event.get_message()
        await button.get_reply_message()
        await event.delete()
        async with Drone.conversation(event.chat_id) as conv:
            xx = await conv.send_message(
                "Send me any image for thumbnail as a reply to this message.")
            x = await conv.get_reply()
            if not x.media:
                xx.edit("No media found.")
            mime = x.file.mime_type
            if "png" not in mime and "jpg" not in mime and "jpeg" not in mime:
                return await xx.edit("No image found.")
            await xx.delete()
            t = await event.client.send_message(event.chat_id, "Trying.")
            path = await event.client.download_media(x.media)
            if os.path.exists(f"{event.sender_id}.jpg"):
                os.remove(f"{event.sender_id}.jpg")
            os.rename(path, f"./{event.sender_id}.jpg")
            await t.edit("Temporary thumbnail saved!")
    else:
        await event.answer("You are not authorized to use this feature.")


@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    if event.sender_id in AUTH:
        event.client
        await event.edit("Trying.")
        try:
            os.remove(f"{event.sender_id}.jpg")
            await event.edit("Removed!")
        except Exception:
            await event.edit("No thumbnail saved.")
    else:
        await event.answer("You are not authorized to use this feature.")


@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "Send me Link of any message to clone it here, For private channel message, send invite link first.\n\n**Fork Maintainer:** @AlphaMaxWolf"
    await start_srb(event, text)


@Drone.on(
    events.NewMessage(incoming=True,
                      from_users=AUTH,
                      pattern="/nuke",
                      func=lambda e: e.is_private))
async def shutdown(event):
    await event.reply("Exited.")
    os._exit(1)
