from ethon.telefunc import force_sub
from pyrogram.errors import FloodWait
from telethon import events

from main.plugins.helpers import get_link, join
from main.plugins.pyroplug import get_msg

from .. import AUTH
from .. import FORCESUB as fs
from .. import Bot
from .. import bot as Drone
from .. import userbot

ft = f"To use this bot you've to join @{fs}."

message = "Send me the message link you want to start saving from, as a reply to this message."


@Drone.on(events.NewMessage(incoming=True, from_users=AUTH))
async def clone(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s:
        await event.reply(r)
        return
    edit = await event.reply("Processing!")
    try:
        if "t.me/+" in link:
            q = await join(userbot, link)
            await edit.edit(q)
            return
        if "t.me/" in link:
            await get_msg(userbot, Bot, Drone, event.sender_id, edit.id, link,
                          0)
    except FloodWait as fw:
        return await Drone.send_message(
            event.sender_id,
            f"Try again after {fw.x} seconds due to floodwait from telegram.",
        )
    except Exception as e:
        print(e)
        await Drone.send_message(
            event.sender_id,
            f"An error occurred during cloning of `{link}`\n\n**Error:** {str(e)}",
        )
