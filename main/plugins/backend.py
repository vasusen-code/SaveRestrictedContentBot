#Github.com/Vasusen-code
from .. import API_ID, BOT_TOKEN, API_HASH
from pyrogram import Client, filters
import re

Bot = Client(
    "Simple-Pyrogram-Bot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

async def get_msg(client, sender, msg_link):
    chat = msg_link.split("/")[-2]
    msg_id = int(msg_link.split("/")[-1])
    await client.copy_message(sender, chat, msg_id)
    
    
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
    
@Bot.on_message(filters.private)
async def start(bot, event):
    link = get_link(event.text)
    if not link:
        return
    if 't.me' in link:
        try:
            await get_msg(bot, event.chat.id, link)
        except Exception as e:
            return await event.reply(f'Error: `{str(e)}`')

Bot.run()
