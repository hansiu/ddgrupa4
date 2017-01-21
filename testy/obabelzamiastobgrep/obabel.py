import os,sys

#os.system('sudo obabel -isdf ../inputfiles/ligands.sdf -osmi -O../inputfiles/ligands.smi')

grupy_funkcyjne = open('../inputfiles/fragments4.txt','r')

i=1

for line in grupy_funkcyjne:
    grupa = line[:-1]
    #grupa = "*".join(line[:-1].split("[*]"))
    print(grupa)
    os.system("babel ../inputfiles/ligands.sdf ../groups/out"+str(i)+".smi --filter \"s='"+grupa+"'\"")
#"obgrep '"+grupa+"' ../inputfiles/ligands.smi > ../groups/output"+str(i)+".smi")
    i+=1

'''
[*]CC(C)C
4122 molecules converted
126 info messages 308353 audit log messages 
[*]OC1OC(CO)C(O)C(O)C1O
327 molecules converted
126 info messages 246727 audit log messages 
[*]Nc1ccc([*])cc1
2266 molecules converted
126 info messages 278122 audit log messages 
[*]c1ccc(O)cc1
3181 molecules converted
126 info messages 292943 audit log messages 
[*]C1CCCCC1
803 molecules converted
126 info messages 254788 audit log messages 
[*]CCN[*]
8320 molecules converted
126 info messages 376462 audit log messages 
[*]CCC[*]
9645 molecules converted
126 info messages 397684 audit log messages 
[*]CCO[*]
6469 molecules converted
126 info messages 345923 audit log messages 
[*]Oc1ccc([*])cc1
3181 molecules converted
126 info messages 292943 audit log messages 
[*]c1ccc(F)cc1
881 molecules converted
126 info messages 255722 audit log messages 
[*]N1CCOCC1
252 molecules converted
126 info messages 245545 audit log messages 
[*]OCC
6569 molecules converted
126 info messages 347540 audit log messages 
[*]CC([*])C(O)C[*]
4059 molecules converted
126 info messages 306976 audit log messages 
[*]NC(C([*])=O)C(C)C
1059 molecules converted
126 info messages 258444 audit log messages 
[*]C(=O)C1CCCN1[*]
861 molecules converted
126 info messages 255315 audit log messages 
[*]CCC
9963 molecules converted
126 info messages 402772 audit log messages 
[*]NC(C)C([*])=O
2983 molecules converted
126 info messages 289402 audit log messages 
[*]OCc1ccccc1
628 molecules converted
126 info messages 251627 audit log messages 
[*]c1ccc(Cl)cc1
1155 molecules converted
126 info messages 260110 audit log messages 
[*]c1ccnc([*])n1
1859 molecules converted
126 info messages 271636 audit log messages '''



#byHans
