from pymongo import MongoClient

client = MongoClient("mongodb+srv://phunq:aos159753@api-lcrp8.mongodb.net")
db = client.moneylover

test_collection = db.test
spendings_collection = db.spendings