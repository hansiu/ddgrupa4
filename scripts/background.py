from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO
from Bio.PDB import PDBParser
from prepare import get_group_dict
import glob

# in repo
groups = '../groups'
pockets = '../inputfiles/pockets'
background = '../background'
# not in repo
pockets_fasta = '../files/pockets_fasta'
hetero_atms = '../files/hetero'

def count_aa():
	ids = get_group_dict()
	print '!!'
	with open(background+'/all_groups.csv', 'w') as output_groups:
		for gr in sorted(ids.keys()):
			aa_all={}
			all_aa_num = 0
			with open(background+'/'+gr+'.csv', 'w') as output:
				for name in sorted(ids[gr]):
					print gr, name
					record = SeqIO.read(pockets_fasta+'/'+gr+'/'+name+'.fasta', "fasta")
					seq = str(record.seq).replace('X','')
					analysed_seq = ProteinAnalysis(seq)
					aa_pocket = analysed_seq.count_amino_acids()
					aa_num = sum(aa_pocket.values())
					all_aa_num += aa_num
					for aa in sorted(aa_pocket.keys()):
						output.write(name+','+aa+','+str(float(aa_pocket[aa])/aa_num)+'\n')
						if aa not in aa_all.keys():
							aa_all[aa] = aa_pocket[aa]
						else:
							aa_all[aa] += aa_pocket[aa]
				for aa in sorted(aa_all.keys()):
					output_groups.write(gr+','+aa+','+str(float(aa_all[aa])/all_aa_num)+'\n')

def count_ions():
	ids = get_group_dict()
	with open(background+'/ions_all_group.csv','w') as output_groups:
		all_ions = set()
		all_groups = {}
		for gr in sorted(ids.keys()):
			gr_ions={}
			for name in sorted(ids[gr]):
				with open(hetero_atms+'/'+gr+'/'+name+'_pocket','r') as f:
					for line in f:
						if line:
							ion = line.split(' ')[0]
							print line.split(' ')[0], gr, name
							all_ions.add(ion)
							if ion not in gr_ions.keys():
								gr_ions[ion] = 0
							gr_ions[ion] +=1
			all_groups[gr] = gr_ions
		for group in sorted(all_groups.keys()):
			for i in all_ions:
				if i not in all_groups[group].keys():
					all_groups[group][i] = 0
			ions_num = sum(all_groups[group].values())
			for ion in sorted(all_groups[group].keys()):
				pr = float(all_groups[group][ion])/ions_num
				output_groups.write(group+','+ion+','+str(pr)+','+str(all_groups[group][ion])+'\n')
				#print ions_num, pr, group, ion
	print 'ALL DONE!'

count_ions()
