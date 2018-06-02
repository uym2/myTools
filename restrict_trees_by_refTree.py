#! /usr/bin/env python

from tree_lib import prune_tree
from dendropy import Tree
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input",required=True,help="Input trees")
parser.add_argument("-r","--reference",required=True,help="Reference tree")
parser.add_argument("-o","--output",required=True,help="Output trees")

args = vars(parser.parse_args())

refTree = Tree.get_from_path(args["reference"],'newick')

leafSet = [ x.taxon.label for x in refTree.leaf_node_iter() ]

with open(args["input"],'r') as fin:
    treein = fin.readlines()

treeout = []
    
for t in treein:
    tree = Tree.get(data=t,schema="newick")
    RS = [ x.taxon.label for x in tree.leaf_node_iter() if x.taxon.label not in leafSet ]
    prune_tree(tree,RS)
    treeout.append(tree.as_string("newick"))
            
with open(args["output"],'w') as fout:
    for t in treeout:
        fout.write(t)
