#! /usr/bin/env python
# Usage: python mask_aln.py <file_in> <path_out> <mask_levels>


from sys import argv
import os.path
from sequence_lib import count_gaps, read_fasta, write_fasta

file_in = argv[1]
path_in,file_name = os.path.split(file_in)
path_out = path_in if (argv[2] == '-') else argv[2] 
base_name,ext = os.path.splitext(file_name)

taxon_names, seq_aln = read_fasta(file_in)
gap_count = count_gaps(seq_aln)
N = len(gap_count)
taxon_count = len(taxon_names)

for msk_lev in argv[3:]:
	gap_limit = taxon_count*(1-float(msk_lev))
	chosen_cols = [i for i in range(N) if gap_count[i] <= gap_limit]
	msk_aln = [""]*taxon_count
	output_file = path_out + "/" + base_name + "_msk" + str(msk_lev) + ext
	for j in chosen_cols:
		for i in range(taxon_count):
			msk_aln[i] = msk_aln[i] + seq_aln[i][j]
	write_fasta(output_file,taxon_names,msk_aln)
			
