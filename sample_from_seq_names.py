#! /usr/bin/env python
# usage: python sample_from_seq_names.py <infile.fasta> <outfile> <list of sequences to be removed>

from sequence_lib import sample_from_list
from sys import argv

infile = argv[1]
outfile = argv[2]
taxalist = argv[3:]

sample_from_list(infile,taxalist,outfile)
