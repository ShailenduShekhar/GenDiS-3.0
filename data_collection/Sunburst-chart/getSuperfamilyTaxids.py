import os
from parseXML_util2 import ReadXML
from parseXML_util2 import TaxonStruct as ts
from alive_progress import alive_bar

'''
    POINTS TO NOTE:

    ~ Superfamily paths currently available: 
        '/home/ibab/sem4/project/data_gendis_3.0/superfamilies/SMS/'
    ~ Superfamily paths used in development:
        '/home/ibab/sem4/project/codes/sunburst_implementation/readyingTheData/test_superfamily'
    ~ As the efetch_xml_files2 are incomplete, we might not get all the taxids that are available in taxid.out files


    DEBUG:
        1. New line character is not getting printed in the output files.
        2. A blank file (103589.csv) was created even though I thought I had put fail safes against such cases. [solved]
        3. writeLineagesToFile is not working [sort of solved]
        4. Look into ts.lineage and check if it can contain all the lineages together.

'''
class OperateOnTaxidFile:
    def __init__(self):
        self.superfamilies_path = [ # should contain the path(s) to the directory containing individual directories of superfamilies
         '/home/ibab/sem4/project/data_gendis_3.0/superfamilies/SMS/'   
        ]
        self.xmlfiles_path = '/home/ibab/sem4/project/data_gendis_3.0/taxdb_ncbi_sep22/efetch_xml_files2'
        self.lineages_file = '/home/ibab/sem4/project/codes/sunburst_implementation/readyingTheData/superfamilyDataForSunburst/SMS/'
        self.output_filename = ''

    def writeLineagesToFile(self,all_superfamily_taxons): # 'all_superfamily_taxons' is a 2D list; each element is a list
        var = open(self.output_filename,'w')
        var.write('Superkingdom,Kingdom,Phylum,Class,Order,Family,Genus,Species\n')
        for taxon in all_superfamily_taxons:
            for index,ele in enumerate(taxon):
                var.write(f'{ele.sciname}\n') if index == len(taxon)-1 else var.write(f'{ele.sciname},')
        var.close()
        return

    def getXMLFiles(self,taxids): # fetches the individual xml files and pushes them to be read
        all_superfamily_taxons = [] # contains the lineages of all the taxids in a particular superfamily
        for taxid in taxids:
            pass_while_loop = False
            xml_directories_list = list(os.scandir(self.xmlfiles_path))
            xml_directories_iterator = 0
            #print(f'number of xml directories : {len(xml_directories_list)}')
            while xml_directories_iterator < len(xml_directories_list):
                xml_dir = xml_directories_list[xml_directories_iterator]
                #print('current xml directory : ' + xml_dir.name)
                if os.path.isdir(xml_dir):
                    for ent in os.scandir(self.xmlfiles_path + '/' + xml_dir.name): # 'ent' is the name of xml file of an individual tax id
                        taxid_in_ent = ent.name[ent.name.find('id=')+3 : ent.name.rfind('&')] # extracting only the taxid out of the filename
                        if taxid == taxid_in_ent:
                            #print('name of xml file' + taxid_in_ent)
                            pass_while_loop = True
                            readxml = ReadXML(ent)
                            readxml.readMain()
                            all_superfamily_taxons.append(ts.lineage.copy())
                            ts.lineage.clear()
                            break
                if pass_while_loop == True: 
                    break
                xml_directories_iterator += 1
        self.writeLineagesToFile(all_superfamily_taxons)
        return

    def openTaxidFile(self,filename): # filename holds the absolute path of the 'taxid.out' file for a particular superfamily
        taxids = [] # finally, holds unique taxids for a particular superfamily taxid_out file
        var = open(filename)
        line = var.readline()
        while(line):
            taxids.append(line.replace('\n',''))
            line = var.readline()
        var.close()
        taxids = set(taxids)
        if len(taxids) > 0:
            self.getXMLFiles(taxids)
        return

    def filesCount(self,dirname): # checks the number of superfamily directories in a particular directory
        count = 0
        for entry in os.scandir(dirname):
            if entry.is_dir(): count += 1
        return count

    def openDirectory(self):
        for path_ in self.superfamilies_path:
            print('Going through the Superfamily Directories in the following path:')
            print('\t\t' + path_)
            with alive_bar(self.filesCount(path_)) as bar:
                for entry in os.scandir(path_): # 'entry' is a directory/file in the 'path_'
                    if entry.is_dir(): # checks if the entry is a directory, which confirms if entry is a superfamily directory
                        taxid_file = f'{entry.path}/{entry.name}_da_out/{entry.name}_taxid.out' # path of taxid file inside the superfamily
                        if os.path.isfile(taxid_file): # checks if the taxid file exists or not
                            self.output_filename = f'{self.lineages_file}{entry.name}.csv'
                            self.openTaxidFile(taxid_file)
                    bar()

ot = OperateOnTaxidFile()
ot.openDirectory()
