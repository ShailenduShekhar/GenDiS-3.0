import os
xml_files_by_taxid = {}  # Dictionary to store XML files grouped by tax ID
xmlfiles_path = '/home/mini/gendis/database/taxdb_ncbi_sep22/efetch_xml_files'
for ent_top in os.scandir(xmlfiles_path):
    for ent in os.scandir(ent_top.path):
        taxid_in_ent = ent.name[ent.name.find('id=')+3 : ent.name.rfind('&')]
        if taxid_in_ent not in xml_files_by_taxid:
            xml_files_by_taxid[taxid_in_ent] = []
            xml_files_by_taxid[taxid_in_ent].append(ent.path)
            
print(xml_files_by_taxid)
