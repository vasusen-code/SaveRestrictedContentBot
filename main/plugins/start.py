import os
from flask import Flask, request, jsonify
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb

S = '/' + 's' + 't' + 'a' + 'r' + 't'

app = Flask(__name__)

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):
    # Your existing code for the callback

@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    # Your existing code for the callback

@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = (
        "Send me the link of any message to clone it here. "
        "For private channel messages, send the invite link first.\n\n"
        "**SUPPORT:** @susanta_support\n\n"
        "Join our channel @susanta_bhndarii for updates and announcements!"
    )
    await start_srb(event, text)

# Add a simple route for Heroku to hit to check if the app is running
@app.route('/')
def index():
    return "Hello, this is your Telegram bot!"

# Run the Flask app if this script is the main script
if __name__ == '__main__':
    # Start the Flask app on a different port than the default one
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
