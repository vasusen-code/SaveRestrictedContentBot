# Save Restricted Content Bot

A simple telegram bot to save restricted content with custom thumbmail support by Mahesh Chauhan.

<p><a href="https://t.me/MaheshChauhan"> <img src="https://img.shields.io/badge/Telegram-blue?style=for-the-badge&logo=telegram&logoColor=white" width="100""/></a></p>

<p align="left"><a href="https://github.com/vasusen-code/saverestrictedcontentbot"><img src="https://github-readme-stats.vercel.app/api/pin?username=vasusen-code&show_icons=true&theme=midnight&hide_border=true&repo=saverestrictedcontentbot"></a></p>
  
Upcoming features:
- Save multiple content at once/Save in range

# Variables

- `API_ID`
- `API_HASH`
- `SESSION` - Telethon string session
Get Telethon string session from [BOT](https://t.me/SessionStringGeneratorZBot) 
- `BOT TOKEN` 
- `FORCESUB` - Public channel username without '@'
  
# Issues
- if you see any message like `ERROR R12` in heroku logs, just restart. 
- `CHANNEL INVALID` if channel not joined. 
- if you face `ERROR: Client has not been started yet` then just send `/start`.

# Deploy
<p><a href="https://heroku.com/deploy"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blue?style=for-the-badge&logo=heroku" width="200""/></a></p>

if deploy button doesn't work, then deploy `manually.`

Buildpacks for manual :

- `heroku/python`
- `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
