#! /usr/bin/env python

# wrapper for dendropy4.calculate.treecompare
# https://pythonhosted.org/DendroPy/library/treecompare.html

# Inputs: 2 arguments - path2tree1 & path2tree2 (newick schema)
# Output: distance measures of 2 trees (branch lengths)

# Ex: python draft0_treecompare.py Tree1 Tree2
import sys
from dendropy import TaxonNamespace,Tree, calculate

tree1_file = sys.argv[1]
tree2_file = sys.argv[2]

tns = TaxonNamespace()
tree1 = Tree.get_from_path(tree1_file,'newick',taxon_namespace=tns)
tree2 = Tree.get_from_path(tree2_file,'newick',taxon_namespace=tns)

tree1.encode_bipartitions()
tree2.encode_bipartitions()

print (calculate.treecompare.euclidean_distance(tree1,tree2))
#print ('Manhattan Distance: '+ str( calculate.treecompare.weighted_robinson_foulds_distance(tree1,tree2)) )
