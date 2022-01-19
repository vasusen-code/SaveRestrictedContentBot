# ChauhanMahesh/Vasusen/COL/DroneBots
# Github.com/Vasusen-code

from telethon import errors
from telethon.tl.functions.messages import ImportChatInviteRequest

async def join(client, invite_link)
    try:
        await client(ImportChatInviteRequest(invite_link))
        return "Successfully joined the Channel"
    except errors.UserAlreadyParticipantError:
        return "Already joined the Channel"
    except errors.InviteHashExpiredError:
        return "Wrong URL"
      
async def get_msg(client, msg_link):
    chat = int(str(-100) + str(msg_link.split("/")[-2]))
    msg_id = int(msg_link.split("/")[-1])
    msg = await client.get_messages(chat, offset_id=msg_id)
    if msg.video:
    
    
