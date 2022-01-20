from pyrogram import Client, filters, idle
from pyrogram.raw.functions.messages import ImportChatInvite
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

import re
from decouple import config

forcesub_text = 'You have to join @Dronebots to use this bot.'

#Multi client-------------------------------------------------------------------------------------------------------------

async def start(Bot, userbot):
    await Bot.start()
    await userbot.start()
    await idle()
    
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

async def forcesub(bot, sender):
    FORCESUB = config("FORCESUB", default=None)
    if FORCESUB is not None:
        if not str(FORCESUB).startswith("-100"):
            FORCESUB = int("-100" + str(FORCESUB))
    if FORCESUB is not None:
        try:
            user = await bot.get_chat_member(FORCESUB, sender)
            if user.status == "kicked":
                return True
        except UserNotParticipant:
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
