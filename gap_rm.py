# input: a file contains sequences (e.g. fasta) with gaps (as such in a groundtruth alignment file)
# output: remove all gaps. The purpose is to obtain unaligned sequences from groundtruth file.

import sys
from sequence_lib import gap_rm

file_in = sys.argv[1]
file_out = sys.argv[2]

fout = open(file_out,'w')

for line in open(file_in,'r'):
	if line[0] != '>':
		sequence = gap_rm(line)
		fout.write(sequence)
	else:
		fout.write(line)

fout.close()

