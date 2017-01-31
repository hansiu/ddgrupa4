import csv
from glob import glob
from collections import OrderedDict

#../background/all_groups.csv
# grupax,A,0.13
bgaafile = open("../background/all_groups.csv")
bgionfile = open("../background/ions_all_group.csv")
bgs_aa={}
bgs_ion={}

#..results oraz ..results_5A/grupax.txt
#ALA\t154
#dwaostatnie ligand_names_with_information,ligand_names_without_information
results = {"3A":"../results/grupa", "5A":"../results_5A/grupa"}

d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

def aa3to1(x):
    x=x.upper()
    if len(x) % 3 != 0: 
        return(False)
    try:
        return(d[x])
    except:
        return(False)

def dict_from_csv():
    bgaa = csv.reader(bgaafile, delimiter=",")
    for line in bgaa:
        try:
            bgs_aa[line[0]][line[1]]=1.0-float(line[2])
        except:
            bgs_aa[line[0]]={line[1]:1.0-float(line[2])}
    bgion = csv.reader(bgionfile, delimiter=",")
    for line in bgion:
        try:
            bgs_ion[line[0]][line[1]]=1.0-float(line[2])
        except:
            bgs_ion[line[0]]={line[1]:1.0-float(line[2])}

def do_calculations_for(rfolder,scale=False):
    wynikiaa={}
    wynikiion={}
    print("Hania!")
    print("...co?")

    for i in range(1,21):
        plik = csv.reader(open(rfolder+str(i)+".txt"), delimiter="\t")
        if scale:
            wagi_aa = bgs_aa["grupa"+str(i)]
            wagi_ion = bgs_ion["grupa"+str(i)]
        wynikiaa[i]={k:0.0 for k in bgs_aa["grupa1"].keys()}
        wynikiion[i]={k:0.0 for k in bgs_ion["grupa1"].keys()}
        print("licze... grupe"+str(i)+"!!!!")

        for line in plik:
            aa=aa3to1(line[0])
            if aa:
                if scale:
                    wynikiaa[i][aa]=int(line[1])*wagi_aa[aa]
                else:
                    wynikiaa[i][aa]=int(line[1])
            else:
                if line[0].startswith('ligands'):
                    pass
                if scale:
                #print(line[0])
                #print(wagi_ion[line[0]])
                #print(int(line[1])*wagi_ion[line[0]])
                    try:
                        wynikiion[i][line[0]]=int(line[1])*wagi_ion[line[0]]
                    except KeyError:
                        pass
                else:
                    try:
                        wynikiion[i][line[0]]=int(line[1])
                    except KeyError:
                        pass
    if scale:
        outaa=csv.writer(open(rfolder[:-5]+"weightedWynikiaa.csv",'w'),delimiter=";")
        oution=csv.writer(open(rfolder[:-5]+"weightedWynikiion.csv",'w'),delimiter=";")
    else:
        outaa=csv.writer(open(rfolder[:-5]+"normalWynikiaa.csv",'w'),delimiter=";")
        oution=csv.writer(open(rfolder[:-5]+"normalWynikiion.csv",'w'),delimiter=";")        
    headersaa=sorted([k for k in bgs_aa["grupa1"].keys()])
    outaa.writerow(["grupa"]+headersaa)
    for key in wynikiaa.keys():
        outaa.writerow([key]+[v for v in OrderedDict(sorted(wynikiaa[key].items())).values()])

    headersion=sorted([k for k in bgs_ion["grupa1"].keys()])
    oution.writerow(["grupa"]+headersion)
    #print(headersion)
    for key in wynikiion.keys():
        oution.writerow([key]+[v for v in OrderedDict(sorted(wynikiion[key].items())).values()])

dict_from_csv()
for res in results.keys():
    do_calculations_for(results[res])
    do_calculations_for(results[res],scale=True)

#byHans
