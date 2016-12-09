# I/O lib for molecular sequences

from os.path import isfile

try:
	import cPickle as pickle
except:
	import pickle

def get_taxon_list(filename):
	taxon_list = []
	for line in open(filename,'r'):
		if line[0] == '>':
			taxon_list = taxon_list + [rstrip(line[1:])]
	return sorted(taxon_list)


def hash_taxon_seq(filename):
	taxon_dict = {}
	f = open(filename,'r')
	for line in f:
		if line[0] == '>':
			taxon_dict[line[1:-1]] = gap_rm(rstrip(f.next()))
	return taxon_dict

def gap_rm(str0,gap='-'):
	str1 = ''
	for c in str0:
		if c != gap:
			str1 =  str1 + c
	return str1

def index_fasta(file_in,file_out=None):
	# only work for fasta format
	f = open(file_in,'r')
	seq_pointers = {}
	fp = 0
	while 1:
		line = f.readline()
		if not line:
			break
		if line[0] == '>':
			seq_pointers[line[1:-1]] = fp
		fp = f.tell()
	if not file_out:
		file_extension = file_in.split('.')[-1]
		file_out = file_in[:-(len(file_extension)+1)]+'.idx'
	fout = open(file_out,'w')
	pickle.dump(seq_pointers,fout)
	f.close()
	fout.close()

def load_index(file_in):
	file_extension = file_in.split('.')[-1]
	file_idx = file_in[:-(len(file_extension)+1)] + '.idx'

	if not isfile(file_idx):
		index_fasta(file_in)

	with open(file_idx) as f:
		seq_pointers = pickle.load(f)

	return seq_pointers

def sample_from_list(file_in,taxa_list,file_out):
	seq_pointers = load_index(file_in)
	with open(file_in,'r') as fin:
		with open(file_out,'w') as fout:	 
			for taxon in taxa_list:
				try:
					fin.seek(seq_pointers[taxon])
					fout.write(fin.readline())
					fout.write(fin.readline())
				except:
					print ('taxon inconsistent in tree and sequence files')


def count_gaps(seq_aln):
	N = len(seq_aln[0])
	gap_count = [0]*N
	for seq in seq_aln:
		for i in range(N):
			gap_count[i] += (seq[i] == '-')
	return gap_count

def read_fasta(fas_file):
	taxon_names = []
	seq_aln = []
	with open(fas_file,'r') as f:
		for line in f:
			if line[0] == '>':
				taxon_names.append(rstrip(line))
			else:
				seq_aln.append(rstrip(line))
	return taxon_names, seq_aln	

def write_fasta(output_file,taxon_names,seq_aln):
	with open(output_file,'w') as f:
		T = len(taxon_names)
		for i in range(T):
			f.write(taxon_names[i]+"\n")
			f.write(seq_aln[i]+"\n")
