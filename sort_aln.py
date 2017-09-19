#! /usr/bin/env python

from sequence_lib import sort_aln, read_fasta, write_fasta
from sys import argv

filein = argv[1]
fileout = argv[2]

taxon_names, seq_aln = read_fasta(filein)

sorted_names, sorted_aln = sort_aln(taxon_names, seq_aln)

write_fasta(fileout,sorted_names,sorted_aln)
