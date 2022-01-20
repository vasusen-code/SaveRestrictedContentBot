from telethon import errors
from telethon.tl.functions.messages import ImportChatInviteRequest

async def join(client, invite_link):
    try:
        await client(ImportChatInviteRequest(invite_link))
        return "Successfully joined the Channel"
    except errors.UserAlreadyParticipantError:
        return "Already joined the Channel"
    except errors.InviteHashExpiredError:
        return "Wrong URL"
    
async def forcesub(id):
    FORCESUB = config("FORCESUB", default=None)
    if not str(FORCESUB).startswith("-100"):
        FORCESUB = int("-100" + str(FORCESUB))
    ok = False
    try:
        x = await Drone(GetParticipantRequest(channel=int(FORCESUB), participant=int(id)))
        left = x.stringify()
        if 'left' in left:
            ok = True
        else:
            ok = False
    except UserNotParticipantError:
        ok = True 
    return ok
