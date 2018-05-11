#! /usr/bin/env python

from sys import argv
from sequence_lib import read_fasta, write_fasta
from random import sample

inputfile = argv[1]
outputfile = argv[2]
nsites = int(argv[3])

seq_names, seq_aln = read_fasta(inputfile)


sites = sorted(sample(range(len(seq_aln[0])),nsites))

new_aln = []

for a in seq_aln:
    b = ''
    for i in sites:
        b = b + a[i]
    new_aln.append(b)    

write_fasta(outputfile,seq_names,new_aln)
