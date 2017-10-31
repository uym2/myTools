#! /usr/bin/env python
# usage: python sample_from_seq_names.py <infile.fasta> <outfile> <list of sequences to be removed>

from sequence_lib import filter_out_by_list
from sys import argv

infile = argv[1]
outfile = argv[2]
taxalist = argv[3:]

filter_out_by_list(infile,taxalist,outfile)
