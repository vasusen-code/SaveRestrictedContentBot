from telethon import events

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def m(event):
    yy = await force_sub(event.sender_id)
    if yy is True:
        return await event.reply(forcesubtext)
    link = get_link(event.text)
    if not link:
        return
    if 't.me' in link:
        msg_id = int(link.split("/")[-1])
        chat_id = int(str(-100) + str(link.split("/")[-2]))
        try:
            msg = await get_msg(chat_id, msg_id)
        except Exception as e:
            await event.reply(f'Error: `{str(e)}`')
        if msg.video:
            
        else:
