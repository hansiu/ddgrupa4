import os,sys

#os.system('sudo obabel -isdf ../inputfiles/ligands.sdf -osmi -O../inputfiles/ligands.smi')

grupy_funkcyjne = open('../inputfiles/fragments4.txt','r')

i=1

for line in grupy_funkcyjne:
    grupa = line[:-1]
    #grupa = "*".join(line[:-1].split("[*]"))
    print(grupa)
    os.system("obgrep '"+grupa+"' ../inputfiles/ligandsFINAL.smi > ../groups/output"+str(i)+".smi")
    i+=1



#byHans
