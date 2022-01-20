from telethon import errors
from pyrogram.raw.functions.messages import ImportChatInvite
from decouple import config

forcesub_text = 'You have to join @Dronebots to use this bot.'

#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        await client(ImportChatInvite(invite_link))
        return "Successfully joined the Channel"
    except Exception as e:
        print(e)
        if 'already' or 'Already' in str(e):
            return "Already joined."
        else:
            return "Could not join. Maybe your link is expired."
        
#forcesub-------------------------------------------------------------------------------------------------------------

async def forcesub(id):
    FORCESUB = config("FORCESUB", default=None)
    if FORCESUB is not None:
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

#Regex---------------------------------------------------------------------------------------------------------------
#to get the url from event

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
