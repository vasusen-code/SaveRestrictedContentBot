# Tg:ChauhanMahesh/DroneBots
# Github.com/vasusen-code

from .. import ACCESS_CHANNEL
from .. import bot as drone
from main.plugins.helpers import join

from telethon import events

start_text='Send me the link of message you want to copy.\n\nIf from private channel then send invite link first.'

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def u(event):
    link = get_link(event.text)
    if 't.me/+' in link:
        await event.client.send_message(event.chat_id, start_text, reply_to=event.id, buttons=[[Button.inline("Join.", data='join')]])
    await event.forward_to(int(ACCESS_CHANNEL))

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(start_text, buttons=[[Button.url("DEVELOPER", url="t.me/MaheshChauhan")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="join"))
async def join_chat(event):
    await event.edit('Trying to join.')
    button = await event.get_message()
    msg = await button.get_reply_message() 
    link = get_link(msg.text)
    stat = await join(link)
    await event.edit(stat)
