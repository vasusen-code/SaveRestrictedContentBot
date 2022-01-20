import re
from .. import bot as Drone
from telethon import events

async def get_msg(client, sender, msg_link):
    chat = msg_link.split("/")[-2]
    msg_id = int(msg_link.split("/")[-1])
    msg = await client.get_messages(chat, ids=msg_id)
    await client.send_message(sender, msg)
    
    
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
async def x(event):
    link = get_link(event.text)
    if not link:
        return
    if 't.me' in link:
        try:
            await get_msg(Drone, event.sender_id, link)
        except Exception as e:
            return await event.reply(f'Error: `{str(e)}`')
