import os
from parseXML_util2 import ReadXML
from parseXML_util2 import TaxonStruct as ts
from alive_progress import alive_bar

class OperateOnTaxidFile:
    def __init__(self):
        self.superfamilies_path = ['/home/mini/gendis/gendis_sep2022/all_alpha/SMS/', '/home/mini/gendis/gendis_sep2022/all_beta/SMS/', '/home/mini/gendis/gendis_sep2022/alpha_and_beta/SMS/', '/home/mini/gendis/gendis_sep2022/alpha_or_beta/SMS/', '/home/mini/gendis/gendis_sep2022/membrane_proteins/SMS/', '/home/mini/gendis/gendis_sep2022/multidomain_proteins/SMS/', '/home/mini/gendis/gendis_sep2022/small_proteins/SMS/', '/home/mini/gendis/gendis_sep2022/all_alpha/MMS/', '/home/mini/gendis/gendis_sep2022/all_beta/MMS/', '/home/mini/gendis/gendis_sep2022/alpha_and_beta/MMS/', '/home/mini/gendis/gendis_sep2022/alpha_or_beta/MMS/', '/home/mini/gendis/gendis_sep2022/membrane_proteins/MMS/', '/home/mini/gendis/gendis_sep2022/multidomain_proteins/MMS/', '/home/mini/gendis/gendis_sep2022/small_proteins/MMS/']
        #self.xmlfiles_path = '/home/ibab/sem4/project/data_gendis_3.0/taxdb_ncbi_sep22/efetch_xml_files2'
        self.xmlfiles_path = '/home/mini/gendis/database/taxdb_ncbi_sep22/efetch_xml_files'
        #self.lineages_file = '/home/ibab/sem4/project/codes/sunburst_implementation/readyingTheData/superfamilyDataForSunburst/SMS/'
        self.lineages_file = '/home/mini/gendis/GenDiS-3.0/data_collection/Sunburst-chart/sf_sb_csv_2/'
        self.output_filename = ''

    def writeLineagesToFile(self, all_superfamily_taxons, output_filename):
        try:
            with open(output_filename, 'w') as var:
                #print("opening "+ output_filename)
                var.write('Superkingdom,Kingdom,Phylum,Class,Order,Family,Genus,Species\n')
                for taxon in all_superfamily_taxons:
                    for index, ele in enumerate(taxon):
                        var.write(f'{ele.sciname}\n') if index == len(taxon) - 1 else var.write(f'{ele.sciname},')
        except Exception as e:
            print(f"Error writing to {output_filename}: {str(e)}")

    def openTaxidFile(self, filename, xml_files_by_taxid):
        output_filename = f'{self.lineages_file}{os.path.splitext(os.path.basename(filename))[0]}.csv'
        if os.path.exists(output_filename):
            pass
        else:
            var = open(filename)
            line = var.readline()
            taxids = set()  # Collect unique taxids
            while line:
                taxid = line.strip()
                taxids.add(taxid)
                line = var.readline()
            var.close()
            all_superfamily_taxons = []
            for taxid in taxids:
                if taxid in xml_files_by_taxid:
                    for ent in xml_files_by_taxid[taxid]:
                        try:
                            readxml = ReadXML(ent)
                            readxml.readMain()
                            all_superfamily_taxons.append(ts.lineage.copy())
                            ts.lineage.clear()
                        except:
                            print(f'Cant read XML file : {ent.path}')
                else:
                    pass
                
            #output_filename = f'{self.lineages_file}{os.path.splitext(os.path.basename(filename))[0]}.csv'
            if not len(taxids)==0:
                self.writeLineagesToFile(all_superfamily_taxons, output_filename)

    def openDirectory(self):
        xml_files_by_taxid = {}  # Dictionary to store XML files grouped by tax ID

        for ent_top in os.scandir(self.xmlfiles_path):
            for ent in os.scandir(ent_top):
                taxid_in_ent = ent.name[ent.name.find('id=')+3 : ent.name.rfind('&')]
                if taxid_in_ent not in xml_files_by_taxid:
                    xml_files_by_taxid[taxid_in_ent] = []
                    xml_files_by_taxid[taxid_in_ent].append(ent)

        for path_ in self.superfamilies_path:
            print('Going through the Superfamily Directories in the following path:')
            print('\t\t' + path_)
            with alive_bar(len(os.listdir(path_))) as bar:
                for entry in os.scandir(path_):
                    if entry.is_dir():
                        taxid_file = f'{entry.path}/{entry.name}_da_out/{entry.name}_taxid.out'
                        if os.path.isfile(taxid_file):
                            self.openTaxidFile(taxid_file, xml_files_by_taxid)
                    bar()

ot = OperateOnTaxidFile()
ot.openDirectory()
