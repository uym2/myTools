#! /usr/bin/env python

from sequence_lib import read_fasta
from sys import argv

def report_sequence_length(taxon_names, sequences, mapping, idx, remove_gaps = True):
    for i, taxon in enumerate(taxon_names):
        seq_len = len([ x for x in sequences[i] if x != '-']) if remove_gaps else  len(sequences[i])
        if taxon not in mapping:
            mapping[taxon] = [(idx,seq_len)]
        else:
            mapping[taxon].append((idx,seq_len))


mapping = {}

for idx,filename in enumerate(argv[1:]):
    taxon_names, sequences = read_fasta(filename)
    report_sequence_length(taxon_names, sequences, mapping,idx)

max_idx = len(argv)-1

for taxon in mapping:
    string = taxon
    arr = mapping[taxon]
    i = 0
    for idx,seq_len in arr:
         while i < idx:
            string += " 0"
            i += 1
         string += (" " + str(seq_len))
         i += 1
    while i < max_idx:
        string += " 0"
        i += 1
             
    print(string)
