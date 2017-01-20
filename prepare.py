import glob, os

ref_set_path = 'refined-set'
gen_set_path = 'general-set-except-refined'
files_path = 'ligands'

def get_ligands():
	for directory in glob.glob(ref_set_path+'/*'):
		print 'ref',directory
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_ligand.sdf '+files_path+'/')

	for directory in glob.glob(gen_set_path+'/*'):
		print 'gen',directory 
		os.system('cp '+directory+'/'+directory.split('/')[-1]+'_ligand.sdf '+files_path+'/')

	print "I'M DONE!"

#get_ligands()

def glue():
	os.system('cat '+files_path+'/*.sdf > ligands.sdf')
	print 'DONE!'
glue()
