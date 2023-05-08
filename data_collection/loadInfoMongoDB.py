from pymongo import MongoClient
import pickle

client = MongoClient("localhost", 27017,username='Shailendu@1908',password='MongoShailendu@#admiN')
db = client.gendis_3 # the names of the databases become an attribute
coll = db.superfamily # similarly, the names of the collections also become an attribute
with open('available_sf_data.pickle','rb') as rb:
    coll.insert_many(pickle.load(rb))
