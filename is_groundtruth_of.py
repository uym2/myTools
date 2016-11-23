# usage: python is_groundtruth_of <groundtruth> <rawseq>
# Note: this script does NOT check if the groundtruth is free of gap

import sys
from sequence_lib import hash_taxon_seq

gt = sys.argv[1]
test_file = sys.argv[2]

# a convenient but quite rough idea: for a very large number of sequences, buliding and comparing 2 dictionaries on taxons is not a good idea
# took ~3 secs to complete 10,000 seqs
print hash_taxon_seq(gt) == hash_taxon_seq(test_file)
