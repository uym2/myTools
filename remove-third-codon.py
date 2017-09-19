#! /usr/bin/env python

from sequence_lib import read_fasta, write_fasta
from sys import argv

infile=argv[1]
outfile=argv[2]

taxa,seqs = read_fasta(infile)
new_seqs = []
for seq in seqs:
    new_seq = "".join([seq[i] for i in range(len(seq)) if i%3 != 2])
    new_seqs.append(new_seq)

write_fasta(outfile,taxa,new_seqs)
