#Github.com/Vasusen-code

from pyrogram.errors import FloodWait, BadRequest
from telethon import errors, events

import asyncio, subprocess, re, os, time
from pathlib import Path

#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        await client.join_chat(invite_link)
        return "Successfully joined the Channel"
    except BadRequest:
        return "Could not join. Maybe your link is expired or Invalid."
    except FloodWait:
        return "Too many requests, try again later."
    except Exception as e:
        print(e)
        return "Could not join, try joining manually."
    
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
    
#Screenshot---------------------------------------------------------------------------------------------------------------

async def screenshot(video, sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    out = str(video).split(".")[0] + ".jpg"
    cmd = (f"ffmpeg -ss 00:00:00 -i {video} -vframes 1 {out} -y").split(" ")
    process = await asyncio.create_subprocess_exec(
         *cmd,
         stdout=asyncio.subprocess.PIPE,
         stderr=asyncio.subprocess.PIPE)
        
    stdout, stderr = await process.communicate()
    x = stderr.decode().strip()
    y = stdout.decode().strip()
    print(x)
    print(y)
    if os.path.exists(str(Path(out))):
        return out
    else:
        None
        
