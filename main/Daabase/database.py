#Tg:ChauhanMahesh/DroneBots
#Github.com/vasusen-code
import datetime
import motor.motor_asyncio
from .. import MONGODB_URI

SESSION_NAME = 'saverestricted'

class Database:
  
#Connection--------------------------------------------------------------------

    def __init__(self, MONGODB_URI, SESSION_NAME):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
        self.db = self._client[SESSION_NAME]
        self.col = self.db.users

#collection handling---------------------------------------------------------

    def new_user(self, id):
        return dict(id=id, banned=False, api_id=None, api_hash=None, session=None)
           
    async def add_user(self,id):
        user = self.new_user(id)
        await self.col.insert_one(user)
      
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def banning(self, id):
        await self.col.update_one({'id': id}, {'$set': {'banned': True}})
    
    async def is_banned(self, id):
        user = await self.col.find_one({'id': int(id)})
        banned = user.get('banned', False)
        return banned
      
    async def unbanning(self, id):
        await self.col.update_one({'id': id}, {'$set': {'banned': False}})
        
    async def get_users(self):
        users = self.col.find({})
        return users
    
    async def update_session(self, id, session):
        await self.col.update_one({'id': id}, {'$set': {'session': session}})
    
    async def rem_session(self, id):
        await self.col.update_one({'id': id}, {'$set': {'session': None}})
   
    async def update_api_id(self, id, api_id):
        await self.col.update_one({'id': id}, {'$set': {'api_id': api_id}})
    
    async def rem_api_id(self, id):
        await self.col.update_one({'id': id}, {'$set': {'api_id': None}})
        
    async def update_api_hash(self, id, api_hash):
        await self.col.update_one({'id': id}, {'$set': {'api_hash': api_hash}})
    
    async def rem_api_hash(self, id):
        await self.col.update_one({'id': id}, {'$set': {'api_hash': None}})
        
    async def get_credentials(self, id):
        user = await self.col.find_one({'id':int(id)})
        credentials = []
        credentials.append(user.get('api_id', None))
        credentials.append(user.get('api_id', None))
        credentials.append(user.get('session', None))
        return credentials 
   
    
