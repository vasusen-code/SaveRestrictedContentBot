# ChauhanMahesh/Vasusen/COL/DroneBots
# Github.com/Vasusen-code

from pyrogram.types import Message

async def get_msg(client, msg_link):
    chat = msg_link.split("/")[-2]
    msg_id = int(msg_link.split("/")[-1])
    msg = await client.get_messages(chat, msg_id)
    return msg
    
    
