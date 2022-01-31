# Github.com/Vasusen-code

import asyncio

from .. import Bot

from pyrogram import Client, filters 

@Bot.on_message(filters.private & filters.outgoing)
async def _(bot, event):
    if (str(event.text)).lower().startswith("cloning"):
        c = (event.text).split(" ")[1]
        try:
            chat = c.split("-")[0]     
            msg_id = int(c.split("-")[1])
            await Bot.copy_message(event.chat.id, chat, msg_id)
            await event.delete()
        except ValueError:
            await event.edit("Send me only message link or Invite of private channel.")
        except Exception as e:
            if 'username' in str(e):
                await event.edit("Couldn't clone message, maybe i am banned from the given chat.")
            else:
                await event.edit(str(e))
            
