from pyrogram import Client, filters, idle
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

import re
from decouple import config

forcesub_text = 'You have to join @Dronebots to use this bot.'

#Multi client-------------------------------------------------------------------------------------------------------------

async def start_userbot(userbot):
    await userbot.start()
    await idle()
    
#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        hash = 't.me/joinchat/' + invite_link.split("+")[1]
        await client.join_chat(hash)
        return "Successfully joined the Channel"
    except Exception as e:
        print(e)
        if 'INVITE_HASH_EXPIRED' in str(e):
            return "Could not join. Maybe your link is expired."
        elif 'already' or 'Already' in str(e):
            return "Already joined."
        else:
            return f"Error:` {str(e)}`"
        
#forcesub-------------------------------------------------------------------------------------------------------------

async def forcesub(bot, sender):
    FORCESUB = config("FORCESUB", default=None)
    if not str(FORCESUB).startswith("-100"):
        FORCESUB = int("-100" + str(FORCESUB))
    try:
        user = await bot.get_chat_member(FORCESUB, sender)
        if user.status == "kicked":
            return True
    except UserNotParticipant:
        return True
    except Exception as e:
        prit(e)
        return True
        
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
