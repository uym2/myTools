#! /usr/bin/env python

from tree_lib import prune_tree
from dendropy import Tree
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input",required=True,help="Input trees")
parser.add_argument("-o","--output",required=True,help="Output trees")
parser.add_argument("-l","--listing",required=True,help="Removing set")
parser.add_argument("-v","--reverse",required=False,action='store_true',help="Do the reverse pruning: retain the listed taxa. Default: NO")

args = vars(parser.parse_args())

RS = args["listing"].split() if not args["reverse"] else None

with open(args["input"],'r') as fin:
    treein = fin.readlines()

treeout = []
    
for t in treein:
    tree = Tree.get(data=t,schema="newick",preserve_underscores=True)
    if not RS:
        RS = [ x.taxon.label for x in tree.leaf_node_iter() if x.taxon.label not in args["listing"].split() ]
    prune_tree(tree,RS)
    treeout.append(tree.as_string("newick", unquoted_underscores=True))
            
with open(args["output"],'w') as fout:
    for t in treeout:
        fout.write(t)

