import re

from .. import API_ID, API_HASH, BOT_TOKEN

from pyrogram import Client, filters
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
    
@robot.on_message(filters.private)
async def run(client, message):
    link = get_link(message.text)
    if not link:
        return
    if 't.me' in link:
        try:
            await get_msg(robot, message.sender.id, link)
        except Exception as e:
            return await message.reply(f'Error: `{str(e)}`')

robot.run()
