#! /usr/bin/env python

### dendropy4 4.2.0
### https://pythonhosted.org/DendroPy/primer/phylogenetic_distances.html

import sys
import dendropy4

tree = dendropy4.Tree.get(
    path = sys.argv[1],
    schema = "newick")
pdc = tree.phylogenetic_distance_matrix()

#for i, t1 in enumerate(tree.taxon_namespace[:-1]):
#    for t2 in tree.taxon_namespace[i+1:]:
#        print("Distance between '%s' and '%s': %s" % (t1.label, t2.label, pdc(t1, t2)))

print "Mean Pairwise Distance: ", pdc.mean_pairwise_distance()
