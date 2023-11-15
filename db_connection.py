from motor import motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import os

connection_string: str =  'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

client: AsyncIOMotorClient = motor_asyncio.AsyncIOMotorClient(connection_string)
db: AsyncIOMotorDatabase = client.fastapidb