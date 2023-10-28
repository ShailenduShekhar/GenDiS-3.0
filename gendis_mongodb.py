from pymongo import MongoClient


client = MongoClient("localhost", 27017,username='Shailendu@1908',password='MongoShailendu@#admiN')
db = client.gendis_3 # the names of the databases become an attribute
sf_coll = db.superfamily # similarly, the names of the collections also become an attribute
cl_coll = db.classes
cl_sf_dict = {'46456': db.a_sf, '48724': db.b_sf, '51349': db.c_sf, '53931': db.d_sf, '56572':db.e_sf, '56835': db.f_sf, '56992': db.g_sf}