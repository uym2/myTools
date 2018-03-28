#! /usr/bin/env python
# normalize all tree branch by the average root-to-tip distance


from sys import argv
from dendropy import Tree

infile = argv[1]
outfile = argv[2]

tree = Tree.get_from_path(infile,"newick")

tree.seed_node.depth = 0
height = 0
leaf_count = 0


for node in tree.preorder_node_iter():
    try:        
        node.depth = node.parent_node.depth + node.edge_length
    except:    
        continue

    if node.is_leaf():
        height += node.depth
        leaf_count += 1
        
height /= float(leaf_count)

for node in tree.preorder_node_iter():
    try:
        node.edge_length /= height            
    except:
        continue

tree.write_to_path(outfile,"newick")
