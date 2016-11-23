#! /usr/bin/env python
# usage: python sample_from_subtree.py <seq_file.fasta> <subtree.tre>

from sequence_lib import sample_from_list
from tree_lib import get_taxa
from sys import argv

in_file = argv[1]
subtree = argv[2]
out_file = argv[3]


taxa_list = get_taxa(subtree)
sample_from_list(in_file,taxa_list,out_file)
