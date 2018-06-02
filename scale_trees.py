#! /usr/bin/env python
# normalize all tree branch by the average root-to-tip distance


from sys import argv
from dendropy import Tree

infile = argv[1]
outfile = argv[2]
scale = float(argv[3])

outTrees = []

with open(infile,'r') as fin:
    for line in fin:
        try:
            tree = Tree.get(data = line, schema="newick")
        except:
            continue            
        for node in tree.preorder_node_iter():
            try:
                node.edge_length *= scale
            except:
                continue
        outTrees.append(tree.as_string("newick"))    

with open(outfile,'w') as fout:
    for tree in outTrees:
        fout.write(tree)
