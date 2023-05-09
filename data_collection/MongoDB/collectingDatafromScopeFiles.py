import pickle
import json
"""
from pymongo import MongoClient

client = MongoClient("localhost", 27017,username='Shailendu@1908',password='MongoShailendu@#admiN')
db = client.gendis_3 # the names of the databases become an attribute
coll = db.superfamily # similarly, the names of the colls also become an attribute
#coll_docs_list = coll.find()
"""

"""

Format of storing data in MongoDB:

    post = {
       _id : sf_code,
       des : description,
       scop_cl: 'number here',
       scop_cf: 'number here'
    }

"""
class CollectDataFromScope:
    def __init__(self):
        self.post_count = 0
        self.post_list = []

    def getClFl(self,post): # colecting class and fold information of a superfamily from the dir.cla file
        with open("/home/ibab/sem4/project/data_gendis_3.0/dir.cla.scope.2.08-stable.txt") as dar:
            for line in dar:
                if line[0] != "#":
                    li = line.split(',')
                    if li[2] == f"sf={post['_id']}": 
                        post.update({ "scop_cl":li[0].split("\t")[-1][3:], "scop_cf":li[1][3:] })
                        return

    def getIdDes(self): # collecting sf id and description information from the dir.cla file
        with open("/home/ibab/sem4/project/data_gendis_3.0/dir.des.scope.2.08-stable.txt") as var:
            for line in var:
                li = line.split("\t")
                if line[0] != "#":
                    if li[1] == "sf":
                        post = {}; post.update({"_id": li[0],"des": li[-1].replace('\n','')})
                        self.getClFl(post)
                        self.post_list.append(post)
                        #print(post)
                        self.post_count += 1
        print(self.post_count)

    def serialize(self):
        with open('scopid_des_class_fold2.pickle','wb') as wr:
            pickle.dump(self.post_list,wr)

    def serializeJSON(self):
        with open('scopid_des_class_fold2.pickle','wb') as wr:
            pickle.dump(json.dumps(self.post_list),wr)

    def toJSON(self):
        with open('scopid_des_class_fold.json','w') as wr:
            wr.write(json.dumps(self.post_list))
        
coll = CollectDataFromScope()
coll.getIdDes()
coll.serialize()
