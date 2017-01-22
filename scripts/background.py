from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO
from prepare import get_group_dict
import glob

# in repo
groups = '../groups'
pockets = '../inputfiles/pockets'
background = '../background'
# not in repo
pockets_fasta = '../files/pockets_fasta'

def count_aa():
	ids = get_group_dict()
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
#count_aa()
				
