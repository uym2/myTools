#! /usr/bin/env python

from sequence_lib import read_fasta, p_distance
from sys import argv

seq_file = argv[1]

names,aln = read_fasta(seq_file)

d = 0
#count = 0
for i,a1 in enumerate(aln):
    for j,a2 in enumerate(aln[i+1:]):
        d += p_distance(a1,a2)
        #count += 1
L = len(aln)
print(2*d/(L*(L-1)))
