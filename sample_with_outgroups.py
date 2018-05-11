# ! /usr/bin/env python

# sample a tree with specified number of ingroups and outgroups

from tree_lib import sample_with_outgroups
from sys import argv
from dendropy import Tree

treefile = argv[1]
n_ingroups = int(argv[2])
n_outgroups = int(argv[3])
n_reps = int(argv[4])

tree = Tree.get_from_path(treefile,'newick')

check,samples = sample_with_outgroups(tree, n_ingroups, n_outgroups=n_outgroups, n_reps=n_reps)

if not check:
    print("The tree is not large enough for this sampling size!")
else:
    for t,igs,ogs in samples:
        #print(igs,ogs)
        print(t.as_string('newick'))


