#! /usr/bin/env python

from sys import argv
from sequence_lib import read_fasta

input_file = argv[1]

names,sequences = read_fasta(input_file)

total = 0
freq =  {}

for s in sequences:
    for c in s:
        if c != '-':
            total += 1
            if not c in freq:
                freq[c] = 1
            else:
                freq[c] = freq[c] + 1


for c in sorted(freq):
    print(c + " " + str(float(freq[c])/total))
			
