# Don't deploy upto next update(batch for pvt), stay connected to @MaheshChauhan on tg. 

<h1 align="center">
  <b>Save restricted content Bot</b>
</h1> 

Contact: [Telegram](https://t.me/MaheshChauhan)

A stable telegram bot to get restricted messages with custom thumbnail support , made by @MaheshChauhan. 

- works for both public and private channels
- Custom thumbnail support for Pvt medias
- supports text and webpage media messages
- Faster speed
- Forcesubscribe available 
- `/batch` - (For owner only) Use this command to save upto 100 files from a pvt restricted channel at once.

# Variables

- `API_ID`
- `API_HASH`
- `SESSION`
- `BOT TOKEN` 
- `AUTH` - Owner user id
- `FORCESUB` - Public channel username without '@'. Don't forget to add bot in channel as administrator. 

# Get API & TELETHON string session from:
 
API: [API scrapper Bot](https://t.me/USETGSBOT) or [Telegram.org](https://my.telegram.org/auth)

TELETHON SESSION: [SessionGen Bot](https://t.me/SessionStringGeneratorZBot) or [![Run on Repl.it](https://replit.com/badge/github/vasusen-code/saverestrictedcontentbot)](https://replit.com/@SpEcHiDe/GenerateStringSession)

BOT TOKEN: @Botfather on telegram

# Deploy
  
- Fork the repo, and star it
- create app in heroku
- go to settings of app>> config vars>> add all variables
- add buildpacks
- connect to github and deploy
- turn on dynos
  
Buildpacks for manual deploy:

- `heroku/python`
- `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`

# Upcoming features:

- Save multiple content at once/Save in range for public channels
