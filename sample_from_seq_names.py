#! /usr/bin/env python
# usage: python sample_from_subtree.py <seq_file.fasta> <subtree.tre>

from sequence_lib import sample_from_list
from sys import argv

seq_file = argv[1]
name_file = argv[2]
out_file = argv[3]

with open(name_file,'r') as f:
	taxa_list = [line[:-1] for line in f]

sample_from_list(in_file,taxa_list,out_file)
