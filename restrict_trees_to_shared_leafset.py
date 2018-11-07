#! /usr/bin/env python

from tree_lib import prune_tree
from dendropy import Tree
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input",required=True,help="Input trees")
parser.add_argument("-o","--output",required=True,help="Output trees")

args = vars(parser.parse_args())

leafSet = None

with open(args["input"],'r') as fin:
    treein = fin.readlines()

treeout = []

# NOTE: this is NOT a good implementation!
    
for t in treein:
    tree = Tree.get(data=t,schema="newick")
    S = set([ x.taxon.label for x in tree.leaf_node_iter() ])
    leafSet = leafSet.intersection(S) if leafSet is not None else S

for t in treein:
    tree = Tree.get(data=t,schema="newick")    
    RS = [ x.taxon.label for x in tree.leaf_node_iter() if x.taxon.label not in leafSet ]
    prune_tree(tree,RS)
    treeout.append(tree.as_string("newick"))
            
with open(args["output"],'w') as fout:
    for t in treeout:
        fout.write(t)
