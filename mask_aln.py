#! /usr/bin/env python

from sys import argv
from sequence_lib import count_gaps, read_fasta, write_fasta

file_name = argv[1]

taxon_names, seq_aln = read_fasta(file_name)
gap_count = count_gaps(seq_aln)
N = len(gap_count)
taxon_count = len(taxon_names)

for msk_lev in argv[2:]:
	gap_limit = taxon_count*(1-float(msk_lev))
	chosen_cols = [i for i in range(N) if gap_count[i] <= gap_limit]
	msk_aln = [""]*taxon_count
	output_file = file_name + "_msk" + str(msk_lev)
	for j in chosen_cols:
		for i in range(taxon_count):
			msk_aln[i] = msk_aln[i] + seq_aln[i][j]
	write_fasta(output_file,taxon_names,msk_aln)
			
