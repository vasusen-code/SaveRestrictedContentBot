#Github.com/Vasusen-code

import os
from .. import bot, ACCESS
from telethon import events, Button, TelegramClient

st = "Send me Link of any message to clone it here, For private channel message, send invite link first.\n\nSUPPORT: @TeamDrone\nDEV: @MaheshChauhan"

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                              [Button.inline("SET THUMB.", data="sett"),
                               Button.inline("REM THUMB.", data="remt")]
                              ])
    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await event.client.send_message(int(ACCESS), f'{tag} started the BOT\nUserID: {event.sender_id}') 
                        
@bot.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@bot.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
    
    
