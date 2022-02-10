#Tg:MaheshChauhan/DroneBots
#Github.com/Vasusen-code

from telethon import events

async def get_pvt_content(event, chat, id):
    msg = await event.client.get_messages(chat, ids=id)
    await event.client.send_message(event.chat_id, msg) 

async def get_res_content(event, chat, id):
    msg = await event.client.get_messages(chat, ids=id)
    try:
        if msg.media:
            await event.client.download_media(msg.document)
async def private_batch(event, link, _range):
    if not 
