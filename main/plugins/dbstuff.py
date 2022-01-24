#tg:chauhanMahesh/DroneBots
#github.com/vasusen-code
 
from .. import Drone, AUTH_USERS, MONGODB_URI
from telethon import events, Button
from decouple import config
from main.Database.database import Database

#Database command handling--------------------------------------------------------------------------

db = Database(MONGODB_URI, 'videoconvertor')

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def incomming(event):
    if not await db.is_user_exist(event.sender_id):
        await db.add_user(event.sender_id)

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="/users"))
async def listusers(event):
    xx = await event.reply("Counting total users in Database.")
    x = await db.total_users_count()
    await xx.edit(f"Total user(s) {int(x)}")

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="/bcast"))
async def bcast(event):
    ids = []
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("reply to a mesage to broadcast!")
    xx = await event.reply("Counting total users in Database.")
    x = await db.total_users_count()
    await xx.edit(f"Total user(s) {int(x)}")
    all_users = await db.get_users()
    sent = []
    failed = []
    async for user in all_users:
        user_id = user.get("id", None) 
        ids.append(user_id)
    for id in ids:
        try:
            try:
                await event.client.send_message(int(id), msg)
                sent.append(id)
                await xx.edit(f"Total users : {x}", 
                             buttons=[
                                 [Button.inline(f"SENT: {len(sent)}", data="none")],
                                 [Button.inline(f"FAILED: {len(failed)}", data="none")]])
                await asyncio.sleep(1)
            except FloodWaitError as fw:
                await asyncio.sleep(fw.seconds + 10)
                await event.client.send_message(int(id), msg)
                sent.append(id)
                await xx.edit(f"Total users : {x}", 
                             buttons=[
                                [Button.inline(f"SENT: {len(sent)}", data="none")],
                                [Button.inline(f"FAILED: {len(failed)}", data="none")]])
                await asyncio.sleep(1)
        except Exception:
            failed.append(id)
            await xx.edit(f"Total users : {x}", 
                             buttons=[
                                 [Button.inline(f"SENT: {len(sent)}", data="none")],
                                 [Button.inline(f"FAILED: {len(failed)}", data="none")]])
    await xx.edit(f"Broadcast complete.\n\nTotal users in database: {x}", 
                 buttons=[
                     [Button.inline(f"SENT: {len(sent)}", data="none")],
                     [Button.inline(f"FAILED: {len(failed)}", data="none")]])
    
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="^/disallow (.*)" ))
async def bban(event):
    c = event.pattern_match.group(1)
    if not c:
        await event.reply("Disallow who!?")
    AUTH = config("AUTH_USERS", default=None)
    admins = []
    admins.append(f'{int(AUTH)}')
    if c in admins:
        return await event.reply("I cannot ban an AUTH_USER")
    xx = await db.is_banned(int(c))
    if xx is True:
        return await event.reply("User is already disallowed!")
    else:
        await db.banning(int(c))
        await event.reply(f"{c} is now disallowed.")
    admins.remove(f'{int(AUTH)}')
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="^/allow (.*)" ))
async def unbban(event):
    xx = event.pattern_match.group(1)
    if not xx:
        await event.reply("Allow who?")
    xy = await db.is_banned(int(xx))
    if xy is False:
        return await event.reply("User is already allowed!")
    await db.unbanning(int(xx))
    await event.reply(f"{xx} Allowed! ")
    

    


   
    
