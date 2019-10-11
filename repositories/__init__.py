from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mongoData
posts = db.rest_user
token_db=db.access_tokens