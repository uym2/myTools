#! /usr/bin/env python

# usage: compare taxons of two fas (fasta) files
# python compare_taxons <file1> <file2>
# this function written to roughly compare if a fasta file is the groundtruth of another file
# but can be used for other purposes (not yet known)
# if 1 file is the groundtruth of the other, the 2 must share a same set of taxons (the reverse is NOT true)

import sys
from sequence_lib import get_taxon_list


file1 = sys.argv[1]
file2 = sys.argv[2]

print ('Reading file 1')
taxon_list1 = get_taxon_list(file1)
print ('Reading file 2')
taxon_list2 = get_taxon_list(file2)

if taxon_list1 == taxon_list2:
	print('Same taxons!')
else:
	print('Taxons different!')
