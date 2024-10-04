from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from twitter import twitter

uri = "mongodb+srv://anachury:<db_password>@sebastianelmejorprofe.kjfox.mongodb.net/?retryWrites=true&w=majority&appName=SebastianElMejorProfe"

client = MongoClient(uri, server_api=ServerApi('1'))


dbMongo = client ["THEOLDBIRD"]
coleccion = dbMongo["users"]

def save_one(doc):
    coleccion.insert_one(doc)
    
def save_many(docs):
    coleccion.insert_many(docs)