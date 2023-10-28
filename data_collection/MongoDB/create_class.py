import os
import pickle
from pymongo import MongoClient
client = MongoClient("localhost", 27017, username='Shailendu@1908', password='MongoShailendu@#admiN')
db = client.gendis_3  # the names of the databases become an attribute
"""
coll = db.classes
d = [{'_id': '46456', 'des': 'a: All alpha proteins', 'num_fold': 290, 'num_sf':519, 'num_seq': 33745701, 'num_tp': 20690279,},
     {'_id': '48724', 'des': 'b: All beta proteins', 'num_fold': 180, 'num_sf': 374, 'num_seq': 36009271, 'num_tp': 21973707, },
     {'_id': '51349', 'des': 'c: Alpha and beta proteins (a/b)', 'num_fold': 148, 'num_sf': 247, 'num_seq':  67224602, 'num_tp': 53394941, },
     {'_id': '53931', 'des': 'd: Alpha and beta proteins (a+b)', 'num_fold': 396, 'num_sf': 578, 'num_seq':  48232485, 'num_tp': 34602755, },
     {'_id': '56572', 'des': 'e: Multi-domain proteins (alpha and beta)', 'num_fold': 74, 'num_sf': 73, 'num_seq':  5315902, 'num_tp': 3726663, },
     {'_id': '56835', 'des': 'f: Membrane and cell surface proteins and peptides', 'num_fold': 69, 'num_sf': 130, 'num_seq':  5867215, 'num_tp': 3991323, },
     {'_id': '56992', 'des': 'g: Small proteins', 'num_fold': 100, 'num_sf': 139, 'num_seq':  6003912, 'num_tp': 4053609, }]

coll.insert_many(d)
"""
ls = os.listdir('pkls')
class_list = ['all_alpha', 'all_beta', 'alpha_and_beta', 'alpha_or_beta', 'membrane_proteins', 'multidomain_proteins', 'small_proteins']

for file in ls:
     if 'all_alpha' in file:
          sf_coll = db.a_sf
          with open(f'pkls/{file}', 'rb') as f:
               sf_coll.insert_many(pickle.load(f))
     elif 'all_beta' in file:
          sf_coll = db.b_sf
          with open(f'pkls/{file}', 'rb') as f:
               sf_coll.insert_many(pickle.load(f))
     elif 'alpha_and_beta' in file:
          sf_coll = db.d_sf
          with open(f'pkls/{file}', 'rb') as f:
               sf_coll.insert_many(pickle.load(f))
     elif 'alpha_or_beta' in file:
          sf_coll = db.c_sf
          with open(f'pkls/{file}', 'rb') as f:
               sf_coll.insert_many(pickle.load(f))
     elif 'membrane_proteins' in file:
          sf_coll = db.e_sf
          with open(f'pkls/{file}', 'rb') as f:
               sf_coll.insert_many(pickle.load(f))
     elif 'multidomain_proteins' in file:
          sf_coll = db.f_sf
          with open(f'pkls/{file}', 'rb') as f:
               sf_coll.insert_many(pickle.load(f))
     elif 'small_proteins' in file:
          sf_coll = db.g_sf
          with open(f'pkls/{file}', 'rb') as f:
               sf_coll.insert_many(pickle.load(f))