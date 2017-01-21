# Inputfiles preparation

from Bio import SeqIO
import glob, os

# not in repo
ref_set_path = '../refined-set' 
gen_set_path = '../general-set-except-refined'
files_path = '../files'
pockets_fasta = '../files/pockets_fasta'
ligands_mol2 = '../files/ligands_mol2'
# in repo
groups = '../groups'
inputfiles_path = '../inputfiles'

def get_ligands():
	for directory in glob.glob(ref_set_path+'/*'):
		print 'ref',directory
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_ligand.mol2 '+files_path+'/ligands_mol2/')

	for directory in glob.glob(gen_set_path+'/*'):
		print 'gen',directory 
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_ligand.mol2 '+files_path+'/ligands_mol2/')

	print "I'M DONE!"

def get_pockets():
	for directory in glob.glob(ref_set_path+'/*'):
		print 'ref',directory
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_pocket.pdb '+files_path+'/pockets/')

	for directory in glob.glob(gen_set_path+'/*'):
		print 'gen',directory 
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_pocket.pdb '+files_path+'/pockets/')

	print "I'M DONE!"

def get_pockets_fasta():
	for file in glob.glob(files_path+'/pockets/*'):
		print file
		name = file.split('/')[-1].split('_')[0]
		c = SeqIO.convert(file, "pdb-atom", files_path+'/pockets_fasta/'+name+".fasta", "fasta")
	print "I'M DONE!"

def glue_ligands():
	os.system('cat '+files_path+'/*.sdf > ../ligands.sdf')
	print "I'M DONE!"

def get_ids(file_name):
	l = []
	with open(file_name, 'r') as f:
		for line in f:
			l.append(line.split('_')[0])
	return l

def get_group_dict():
	ids = {}
	for file in glob.glob(groups+'/*.txt'):
		gr=file.split('.txt')[0].split('_')[-1]
		ids[gr] = get_ids(file)
	return ids

def sort_pocket_groups():
	ids = get_group_dict()
	for gr in ids.keys():
		d = inputfiles_path+'/pockets/'+gr
		try:
			os.mkdir(d)
		except:
			print 'Directory '+d+' already exists'
		for name in ids[gr]:
			os.system('cp '+inputfiles_path+'/pockets/'+name+'_pocket.pdb '+d+'/')
	print 'ALL DONE!'

def sort_ligands_groups():
	ids = get_group_dict()
	for gr in ids.keys():
		d = ligands_mol2+'/'+gr
		try:
			os.mkdir(d)
		except:
			print 'Directory '+d+' already exists'
		for name in ids[gr]:
			os.system('cp '+ligands_mol2+'/'+name+'_ligand.mol2 '+d+'/')
	print 'ALL DONE!'

