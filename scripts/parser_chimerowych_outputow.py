from glob import glob

zones_path = "../zones/"


def aminocid_counter(path):
    ligand_names_with_information = set()
    ligand_names_without_information = set()
    aminoacids = {}
    for plik in glob(path+"/*ligand*"):
        with open(plik) as f:
            opened = f.readlines()
            if len(opened) is not 0:
                ligand_names_with_information.add(plik[:-6])
                for linia in opened:
                    try:
                        aminoacids[linia.split()[1]] += 1
                    except KeyError:
                        aminoacids[linia.split()[1]] = 0
                    else:
                        ligand_names_without_information.add(plik[:-6])
                    
    plik = open("../results/"+path[9:]+".txt","w")
    for key in aminoacids:
        plik.write(str(key)+"\t"+str(aminoacids[key])+"\n")

    plik.write("ligand_names_with_information"+"\t"+str(len(ligand_names_with_information))+"\n")
    plik.write("ligand_names_without_information"+"\t"+str(len(ligand_names_without_information))+"\n")


for path in glob(zones_path+"*"):
    aminocid_counter(path)
