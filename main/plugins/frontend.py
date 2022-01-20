from .. import bot as drone
from telethon import events

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def u(event):
    if 't.me/+' event.text:
      
