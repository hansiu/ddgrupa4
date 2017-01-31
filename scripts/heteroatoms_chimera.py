import os
from chimera import runCommand as rc

def set_dir(group):
	os.chdir("/home/joanna/Pulpit/Leki_projekt/ddgrupa4/inputfiles/pockets/grupa{}".format(group))

def read_dir(group):
	set_dir(group)
	pocket_list = os.listdir(os.curdir)
	return(pocket_list)

def select_hetero(group):
	set_dir(group)
	pocket_list = read_dir(group)
	for pocket in pocket_list:
		rc("open " + os.curdir + "/{}".format(pocket))
		rc("select " + "#0::.het")
		rc("show sel")
		rc("writesel " + "/home/joanna/Pulpit/Leki_projekt/ddgrupa4/hetero/grupa{}/{}".format(group,pocket.strip(".pdb")) + " namingStyle simple")
		rc("close all")

select_hetero(1)
select_hetero(2)
select_hetero(3)
select_hetero(4)
select_hetero(5)
select_hetero(6)
select_hetero(7)
select_hetero(8)
select_hetero(9)
select_hetero(10)
select_hetero(11)
select_hetero(12)
select_hetero(13)
select_hetero(14)
select_hetero(15)
select_hetero(16)
select_hetero(17)
select_hetero(18)
select_hetero(19)
select_hetero(20)
