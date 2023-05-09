import sys

class TaxonStruct:
    lineage = [] # finally, contains the whole lineage, starting from the highest order
    def __init__(self,taxid,sciname,rank):
        self.taxid = taxid
        self.sciname = sciname
        self.rank = rank

class ReadXML:
    draft_lineage = []
    rank_list = ['superkingdom','kingdom','phylum','class','order','family','genus','species']
    def __init__(self,xmlfile):
        self.xmlfile = open(xmlfile)
    def readMain(self):
        hold_taxon = []
        line = self.xmlfile.readline()
        while(line):
            if '<TaxId>' in line:
                taxid = line[line.find('>')+1:line.find('</')]
                hold_taxon.append(taxid)
            elif '<ScientificName>' in line:
                sciname = line[line.find('>')+1:line.find('</')]
                hold_taxon.append(sciname)
            elif '<Rank>' in line:
                rank = line[line.find('>')+1:line.find('</')]
                hold_taxon.append(rank)
            if len(hold_taxon) == 3:
                self.draft_lineage.append(TaxonStruct(hold_taxon[0],hold_taxon[1],hold_taxon[2]))
                hold_taxon.clear()
            line = self.xmlfile.readline()
        self.checkRanks()
    def checkRanks(self):
        first_ele = self.draft_lineage.pop(0)
        self.draft_lineage.append(first_ele)
        for rank in self.rank_list:
            check = False
            for taxon in self.draft_lineage:
                if rank == taxon.rank:
                    TaxonStruct.lineage.append(taxon)
                    check = True
            if check == False:
                TaxonStruct.lineage.append(TaxonStruct('None','None','None'))
        self.draft_lineage.clear()
'''
re = ReadXML(sys.argv[1])
re.readMain()
for ele in ReadXML.draft_lineage:
    print(ele.sciname + '\t' + ele.rank)
print('cleaned starts here : \n')
for ele in TaxonStruct.lineage:
    print(ele.sciname + '\t' + ele.rank)
'''
