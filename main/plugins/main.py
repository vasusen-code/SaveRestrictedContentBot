import re
from telethon import events

from .. import API_ID, API_HASH, BOT_TOKEN
from .. import bot as Drone

from pyrogram import client, filters
from main.plugins.get_msg import get_msg

robot = Client('robot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False
    
@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def m(event):
    pass
  
@robot.on_message(filters.private)
async def run(client, message):
    link = get_link(message.text)
    if not link:
        return
    if 't.me' in link:
        try:
            await get_msg(robot, event.sender_id, link)
        except Exception as e:
            return await message.reply(f'Error: `{str(e)}`')

robot.run()
