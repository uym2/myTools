#! /usr/bin/env python
# sort the sequences in a fasta file based on the postorder of the tree


from sequence_lib import sample_from_list
from dendropy import Tree
from sys import argv

file_in = argv[1]
tree_file = argv[2] 
file_out = argv[3]

tree = Tree.get_from_path(tree_file,'newick')
taxa_list = [node.taxon.label for node in tree.postorder_node_iter() if node.is_leaf()]

sample_from_list(file_in,taxa_list,file_out)
