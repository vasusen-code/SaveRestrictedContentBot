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
