import os
from glob import glob

for folder in glob("../inputfiles/ligands_mol2/grupa*/"):
    print(folder[32:-1])
    os.system("obabel "+folder+"*.mol2 -osdf -O"+folder+"ligands"+folder[32:-1]+".sdf")
