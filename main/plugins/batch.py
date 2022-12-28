#Tg:MaheshChauhan/DroneBots
#Github.com/Vasusen-code

"""
Plugin for both public & private channels!
"""

import time, os, asyncio

from .. import bot as Drone
from .. import userbot, Bot, AUTH
from .. import FORCESUB as fs
from main.plugins.pyroplug import check, get_bulk_msg
from main.plugins.helpers import get_link, screenshot

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from pyrogram import Client 
from pyrogram.errors import FloodWait

from ethon.pyfunc import video_metadata
from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."

batch = []
batch_ = []

async def get_pvt_content(event, chat, id):
    msg = await userbot.get_messages(chat, ids=id)
    await event.client.send_message(event.chat_id, msg) 
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    # wtf is the use of fsub here if the command is meant for the owner? 
    # well am too lazy to clean 
    s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    if s == True:
        await event.reply(r)
        return       
    if f'{event.sender_id}' in batch:
        return await event.reply("You've already started one batch, wait for it to complete you dumbfuck owner!")
    async with Drone.conversation(event.chat_id) as conv: 
        if s != True:
            await conv.send_message("Send me the message link you want to start saving from, as a reply to this message.", buttons=Button.force_reply())
            try:
                link = await conv.get_reply()
                try:
                    _link = get_link(link.text)
                except Exception:
                    await conv.send_message("No link found.")
            except Exception as e:
                print(e)
                return await conv.send_message("Cannot wait more longer for your response!")
            await conv.send_message("Send me the number of files/range you want to save from the given message, as a reply to this message.", buttons=Button.force_reply())
            try:
                _range = await conv.get_reply()
            except Exception as e:
                print(e)
                return await conv.send_message("Cannot wait more longer for your response!")
            try:
                value = int(_range.text)
                if value > 100:
                    return await conv.send_message("You can only get upto 100 files in a single batch.")
            except ValueError:
                return await conv.send_message("Range must be an integer!")
            if s != True:
                await conv.send_message(r)
                return
            batch.append(f'{event.sender_id}')
            batch_.append(f'{event.sender_id}')
            cd = await conv.send_message("**Batch process ongoing.**\n\nProcess completed: ", 
                                    buttons=[[Button.inline("CANCEL❌", data="cancel")]])
            await run_batch(userbot, Bot, event.sender_id, value, cd, _link) 
            conv.cancel()
            batch.clear()
            batch_.clear()
            
@Drone.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
    batch_.clear()
    
async def run_batch(userbot, client, sender, range_, countdown, link):
    for i in range(range_ + 1):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        if not 't.me/c/' in link:
            if i < 25:
                timer = 2
            else:
                timer = 3
        try: 
            check_ = batch_[0]
            count_down = f"**Batch process ongoing.**\n\nProcess completed: {i+1}"
            out = await get_bulk_msg(userbot, client, sender, link, i) 
            if not out == None:
                if out - 5 > 300:
                    await client.send_message(sender, f'You have floodwaits of {out - 5} seconds, cancelling batch') 
                    batch_.clear()
                    break
                else:
                    fw_alert = await client.send_message(sender, f'Sleeping for {out} second(s) due to telegram flooodwait.')
                    await asyncio.sleep(out)
                    await fw_alert.delete()
                    await get_bulk_msg(userbot, client, sender, link, i) 
            protection = await client.send_message(sender, f"Sleeping for `{timer}` seconds to avoid Floodwaits and Protect account!")
            await countdown.edit(count_down)
            await asyncio.sleep(timer)
            await protection.delete()
        except IndexError:
            await client.send_message(sender, "Batch successfully completed!")
            await countdown.delete()
            break
        except Exception as e:
            print(e)
            if not countdown.text == count_down:
                await countdown.edit(count_down)
                
