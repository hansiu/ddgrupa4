from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio import SeqIO
from prepare import get_group_dict
import glob

groups = '../groups'
pockets = '../inputfiles/pockets'
pockets_fasta = '../files/pockets_fasta' #not in repo

def count_aa():
	ids = get_group_dict()
	for gr in ids.keys():
		for name in ids[gr]:
			aa_pocket = {}
			record = SeqIO.read(pockets_fasta+'/'+gr+'/'+name+'.fasta', "fasta")
			counted = []
			seq = str(record.seq).replace('X','')
			break
		break

count_aa()
				

