from glob import glob
import sys

pliki = glob("../groups/*smi")

for plik in pliki:
    znalezione = open(plik,'r')
    lista = open("../groups/ligandy_z_grupa"+plik[16:-4]+".txt",'w')
    for smiles in znalezione:
        nazwa=smiles.split("\t")[1]
        lista.write(nazwa)
    lista.close()
    
