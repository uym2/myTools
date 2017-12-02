#! /usr/bin/env python

from sequence_lib import read_fasta, write_fasta
from sys import argv

seqfile = argv[1]
reducedFile = argv[2] # output
identicalSeqsFile = argv[3] # output

names,sequences = read_fasta(seqfile)

sorted_seqs = sorted((s,i) for i,s in enumerate(sequences))

reduced_names = [names[sorted_seqs[0][1]]]
reduced_seqs = [sorted_seqs[0][0]]

prev_seq = sorted_seqs[0]
L = len(sorted_seqs)
i=1

found_identical = False
first_write = True
with open(identicalSeqsFile,"w") as f:
    while i<L:
        if sorted_seqs[i][0] == sorted_seqs[i-1][0]:
            if not found_identical:
                if not first_write:
                    f.write("\n")
                else:
                    first_write = False
                f.write(names[sorted_seqs[i-1][1]] + " ")
                found_identical = True
            f.write(names[sorted_seqs[i][1]] + " ")
        else:
            reduced_names.append(names[sorted_seqs[i][1]])
            reduced_seqs.append(sorted_seqs[i][0])
            found_identical = False

        i = i+1

write_fasta(reducedFile,reduced_names,reduced_seqs)

