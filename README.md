<h1 align="center">
  <b>Save restricted content Bot</b>
</h1> 

Contact: [Telegram](https://t.me/MaheshChauhan)

A stable telegram bot to get restricted messages with custom thumbnail support , made by Mahesh Chauhan. 

- works for both public and private chats
- Custom thumbnail support for Pvt medias
- supports text and webpage media messages
- Faster speed
- Forcesubscribe available
- To save from bots send link in this format : `t.me/b/bot_username/message_id` (use plus messenger for message_id)
- `/batch` - (For owner only) Use this command to save upto 100 files from a pvt or public restricted channel at once.
- `/cancel` -  Use this to stop batch
- Time delay is added to avoid FloodWait and keep user account safe. 
  
# Variables

- `API_ID`
- `API_HASH`
- `SESSION`
- `BOT_TOKEN` 
- `AUTH` - Owner user id
- `FORCESUB` - Public channel username without '@'. Don't forget to add bot in channel as administrator. 

# Get API & PYROGRAM string session from:
 
API: [API scrapper Bot](https://t.me/USETGSBOT) or [Telegram.org](https://my.telegram.org/auth)

PYROGRAM SESSION: [SessionGen Bot](https://t.me/SessionStringGeneratorRobot) or [![Run on Repl.it](https://replit.com/badge/github/vasusen-code/saverestrictedcontentbot)](https://replit.com/@levinalab/Session-Generator#main.py)

BOT TOKEN: @Botfather on telegram

# Deploy

Deploy on `VPS`

Easy Method:

- Intall docker-compose
- Fill in the variables in docker-compose.yml file using your favorite text editor or nano 
- Start the container 

```
sudo apt install docker-compose -y
nano docker-compose.yml
sudo docker-compose up --build
```

The hard Way:

- Fill vars in your fork in [this](https://github.com/vasusen-code/SaveRestrictedContentBot/blob/master/main/__init__.py) file as shown in this [picture](https://t.me/MaheshChauhan/36)
- enter all the below commands

```
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
python3 -m main
```

- if you want bot to be running in background then enter `screen -S srcb` before `python3 -m main` 
- after `python3 -m main`, click ctrl+A, ctrl+D
- if you want to stop bot, then enter `screen -r srcb` and to kill screen enter `screen -S srcb -X quit`.

Deploy your bot on `Render`

Tutorial - [Click here](https://telegra.ph/SRCB-on-Render-05-17)

Deploy your bot on `heroku`

» Method - 1:
- Star the repo, and fork it in desktop mode
- Go to settings of your forked repo
- Rename your repo by any other name
- Click on  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
 
» Method - 2:
- Star the repo, and fork it in desktop mode
- create app in heroku
- go to settings of app›› config vars›› add all variables
- add buildpacks
- connect to github and deploy
- turn on dynos
  
Buildpacks for manual deploy:

- `heroku/python`
- `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`

Deploy your bot on `Okteto` [Useless]
  
Tutorial for okteto - [click here](https://telegra.ph/Okteto-Deploy-04-01)

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com)
