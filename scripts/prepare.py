import glob, os

ref_set_path = '../refined-set'
gen_set_path = '../general-set-except-refined'
files_path = '../files'


def get_ligands():
	for directory in glob.glob(ref_set_path+'/*'):
		print 'ref',directory
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_ligand.sdf '+files_path+'/ligands/')

	for directory in glob.glob(gen_set_path+'/*'):
		print 'gen',directory 
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_ligand.sdf '+files_path+'/ligands/')

	print "I'M DONE!"

def get_pockets():
	for directory in glob.glob(ref_set_path+'/*'):
		print 'ref',directory
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_pocket.pdb '+files_path+'/pockets/')

	for directory in glob.glob(gen_set_path+'/*'):
		print 'gen',directory 
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_pocket.pdb '+files_path+'/pockets/')

	print "I'M DONE!"

def glue():
	os.system('cat '+files_path+'/*.sdf > ../ligands.sdf')
	print "I'M DONE!"

get_pockets()
