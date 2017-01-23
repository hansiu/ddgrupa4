import os,sys
from glob import glob
from rdkit import Chem
with open("../inputfiles/fragments4.txt","r") as f:
    patterns = f.readlines() 


#for folder in glob("../inputfiles/ligands_mol2/grupa*/"):
    #print(folder[32:-1])
    
count = 1
for pattern in patterns:
    plik = open("../inputfiles/ligands_mol2/grupa"+str(count)+"/indexy"+str(count),"w")
    molecules = Chem.SDMolSupplier("../inputfiles/ligands_mol2/grupa"+str(count)+"/ligands"+str(count)+".sdf")
    patt = Chem.MolFromSmarts(pattern[:-1])
    for mol in molecules:
        if mol is not None:
            plik.write(str(mol.GetSubstructMatches(patt))+"\t"+mol.GetProp('_Name')+"\n")
    count = count+1
    plik.close()
       




    
