import pickle
import glob
import os

class CollDataLabFile():
    def __init__(self, path):
        #self.path = '/home/ibab/sem4/project/data_gendis_3.0/superfamilies/SMS'
        self.path = path 
        self.available_sf = []
        with open('scopid_des_class_fold2.pickle','rb') as rbf:
            self.data = pickle.load(rbf)

    def updateNoOfSequences(self,path,sf_code,dict_): # No. of lines in {sf_code}_all_deltablast_out_accids.txt
        sequences_freq = 0
        try:
            with open(path + f'/{sf_code}_deltablast_out/{sf_code}_all_deltablast_out_accids.txt') as fi:
                for line in fi:
                    if len(line) > 0: sequences_freq += 1
        except FileNotFoundError:
            print(f'No such file: {sf_code}_deltablast_out/{sf_code}_all_deltablast_out_accids.txt')
        dict_.update({'sequences':sequences_freq})
        return dict_

    def updateNoOfTP(self,path,sf_code,dict_): # No of lines in gid files
        sequences_freq = 0
        try: 
            with open(path + f'/{sf_code}_da_out/{sf_code}_gidfile') as fi:
                for line in fi:
                    if len(line) > 0: sequences_freq += 1
        except FileNotFoundError:
            print(f'No such file: {sf_code}_da_out/{sf_code}_gidfile')
        dict_.update({'tp_sequences':sequences_freq})
        return dict_

    def updateSCOPDA(self,path,sf_code,dict_): # No of lines in uniqueda files
        da_freq = 0
        try: 
            with open(path + f'/{sf_code}_da_out/{sf_code}_uniqueda') as fi:
                for line in fi:
                    if len(line) > 0: da_freq += 1
        except FileNotFoundError:
            print(f'No such file: {sf_code}_da_out/{sf_code}_uniqueda')
        dict_.update({'scop_da': da_freq})
        return dict_

    def updatePfamDA(self,path,sf_code,dict_): # this information is not yet available
        dict_.update({'pfam_da': 'NA'})
        return dict_

    def updateGenomes(self,path,sf_code,dict_):
        genome_list = [] 
        try: 
            with open(path + f'/{sf_code}_da_out/{sf_code}_taxid.out') as fi:
                for line in fi:
                    if len(line) > 0: genome_list.append(line)
        except FileNotFoundError:
            print(f'No such file: {sf_code}_da_out/{sf_code}_taxid.out')
        dict_.update({'genomes': len(set(genome_list))})
        return dict_


    def updateDictionary(self,path,sf_code,dict_):
        dict_ = self.updateNoOfSequences(path,sf_code,dict_) # the new dict_ has an additional key - 'sequences'
        dict_ = self.updateNoOfTP(path,sf_code,dict_) # the new dict_ has an additional key - 'tp_sequences'
        dict_ = self.updateSCOPDA(path,sf_code,dict_) # the new dict_ contains additional key - 'SCOP DA'
        dict_ = self.updatePfamDA(path,sf_code,dict_) # the new dict_ contains additional key - 'Pfam DA'
        dict_ = self.updateGenomes(path,sf_code,dict_) # the new dict_ contains additional key - 'Genomes'
        return dict_

    def checkAvailableSuperFamily(self):
        for entity in glob.glob(self.path + '/*'): # entity is path to the file with sf code as its name
            sf_code = entity[entity.rfind('/')+1:]
            if os.path.isdir(entity): # checks if entity is a directory
                for dict_ in self.data: # dict_ here is a dictionary that contains the information about a particular sf
                    if dict_.get('_id') == sf_code:
                        dict_ = self.updateDictionary(entity,sf_code,dict_)
                        self.available_sf.append(dict_)
                        break
    def serialize(self):
        with open('available_sf_data.pickle','wb') as wb:
            pickle.dump(self.available_sf,wb)

rd = '/home/mini/gendis/gendis_sep2022/'
class_list = ['all_alpha', 'all_beta', 'alpha_and_beta', 'alpha_or_beta', 'membrane_proteins', 'multidomain_proteins', 'small_proteins']
dir_list = [f'{rd}{c}/SMS' for c in class_list]
dir_list += [f'{rd}{c}/MMS' for c in class_list]
print(dir_list)
for d in dir_list:
    coll = CollDataLabFile(d)
    coll.checkAvailableSuperFamily()
    coll.serialize()
    n = "_".join(d.split("/")[4:])
    cmd = f'mv available_sf_data.pickle pkls/{n}.pickle'
    os.system(cmd)
quit()
#coll = CollDataLabFile()
#coll.checkAvailableSuperFamily()
#coll.serialize()
