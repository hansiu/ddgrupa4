import os
from chimera import runCommand as rc

def read_dir():
	os.chdir("/home/joanna/Pulpit/Leki_projekt/ddgrupa4/inputfiles/ligands_mol2")
	folders = os.listdir(os.curdir)
	return(folders)

def set_dir(elem_no):
	folders = read_dir()
	os.chdir("/home/joanna/Pulpit/Leki_projekt/ddgrupa4/inputfiles/ligands_mol2/{}".format(folders[elem_no]))

def read_indices(elem_no):
	folders = read_dir()
	set_dir(elem_no)
	with open("indexy{}".format(folders[elem_no].strip("grupa")),"r") as i:
		to_fix = i.readlines()
		to_parse = [x.split("\t") for x in to_fix]
		i.close()
	lig_vs_ind = {}
	for l in to_parse:
		lig_vs_ind[l[1]] = l[0]
	for key in lig_vs_ind:
		lig_vs_ind[key] = lig_vs_ind[key].split("),")
	l_of_ls = []
	for key in lig_vs_ind:
		lig_vs_ind[key] = [y for y in lig_vs_ind[key] if y != ")"]
		for elem in lig_vs_ind[key]:
			l_of_ls.append([key.strip("\n"),elem.lstrip(" (").rstrip(")")])
	for l in l_of_ls:
		l[1] = l[1].split(",")
	for l in l_of_ls:
		l[1] = [elem for elem in l[1] if elem != ""]
		l[1] = [int(num)+1 for num in l[1]]
		l.append(int(len(l[1])))
	return(l_of_ls)
#W kazdej liscie sa trzy elementy - 0-numer ligandu, 1-lista indeksow atomow, 2-ilosc indeksow atomow w liscie

def chimera(string, one, two, a):
	rc("open " + "/home/joanna/Pulpit/Leki_projekt/ddgrupa4/inputfiles/pockets/{}/{}pocket.pdb".format(one,two.strip("ligand")))
	rc("select " + "::HOH")
	rc("show sel")
	rc("delete sel")
	#usuwam wody, ale zostawiam wszelkie jony
	rc("open " + "/home/joanna/Pulpit/Leki_projekt/ddgrupa4/inputfiles/ligands_mol2/{}/{}.mol2".format(one,two))
	rc("select " + string)
	rc("zonesel selected 3 #0")
	rc("show sel")
	rc("writesel" + "/home/joanna/Pulpit/Leki_projekt/ddgrupa4/zones/{}/{}_{}".format(one,two,a) + " namingStyle simple")
	rc("close all")

def process(elem_no):
	ligands = read_indices(elem_no)
	folders = read_dir()
	errors = {}
	for a in range(len(ligands)):
		string = ""
		to_one = folders[elem_no]
		to_two = ligands[a][0]
		for i in xrange(ligands[a][2]):
			string = string + "#1@/serialNumber={} ".format(ligands[a][1][i])
		try:
			chimera(string, to_one, to_two, str(a))
		except:
			errors[ligands[a][0]] = folders[elem_no]
	return(errors)

def save_errors(elem_no):
	folders = read_dir()
	errors = process(elem_no)
	with open("/home/joanna/Pulpit/Leki_projekt/ddgrupa4/zones/{}/!!!_errors_{}".format(folders[elem_no],folders[elem_no]), "w") as err:
		for error in errors:
			err.write(error + "\t" + errors[error])
		err.close()

def execute(number):
	for i in xrange(number):
		process(i)
		save_errors(i)

execute(len(read_dir()))
