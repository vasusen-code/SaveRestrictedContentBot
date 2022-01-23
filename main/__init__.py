#ChauhanMahesh/Vasusen/DroneBots/COL

from decouple import config

# Basics
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None) #pyro session
FORCESUB = config("FORCESUB", default=None) 
ACCESS = config("ACCESS", default=None, cast=int)
