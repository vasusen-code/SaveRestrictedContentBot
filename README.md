<h1 align="center">
  <b>Save restricted content Bot</b>
</h1> 

A stable telegram bot to get restricted messages with custom thumbnail support , made by @MaheshChauhan. 

- works for both public and private channels
- Custom thumbnail support for Pvt medias
- supports text and webpage media messages
- Faster speed
- Forcesubscribe available 
- `/batch` - (For owner only) Use this command to save upto 100 files from a pvt restricted channel at once.

<p><a href="https://t.me/MaheshChauhan"> <img src="https://img.shields.io/badge/Telegram-white?style=for-the-badge&logo=telegram&logoColor=blue" width="100""/></a></p>

<p><a href="https://t.me/TeamDrone"> <img src="https://img.shields.io/badge/Support-white?style=for-the-badge&logo=telegram&logoColor=blue" width="100""/></a></p>

# Variables

- `API_ID`
- `API_HASH`
- `SESSION`
- `BOT TOKEN` 
- `AUTH` - Owner user id
- `FORCESUB` - Public channel username without '@'. Don't forget to add bot in channel as administrator. 

# Get API & TELETHON string session from:

<p><a href="https://t.me/USETGSBOT"> <img src="https://img.shields.io/badge/API scrap Bot-grey?style=for-the-badge&logo=telegram&logoColor=blue" width="100""/></a></p>

<p><a href="https://my.telegram.org/auth"> <img src="https://img.shields.io/badge/Telegram Org-grey?style=for-the-badge&logo=internet" width="100""/></a></p>

<p><a href="https://t.me/SessionStringGeneratorZBot"> <img src="https://img.shields.io/badge/Session Bot-grey?style=for-the-badge&logo=telegram&logoColor=blue" width="100""/></a></p>

[![Run on Repl.it](https://replit.com/badge/github/vasusen-code/saverestrictedcontentbot)](https://replit.com/@SpEcHiDe/GenerateStringSession)

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
