#! /usr/bin/env python

# Inputs: 
#    + a tree file in Newick format 
#    + a file that lists the taxa to be added as polytomies:
#        each line of the file is a polytomy group; the starting species name must ALREADY exist in the tree

# Output:
#   + a tree with all polytomies added


from dendropy import Tree, Node, Taxon
from sys import argv

treefile = argv[1]
infofile = argv[2]
outfile = argv[3]

with open(infofile,'r') as f:
    mapping = {}
    for line in f:
        taxa = line.split()
        mapping[taxa[0]] = taxa[1:]


myTree = Tree.get_from_path(treefile,"newick")

leaves=list(myTree.leaf_node_iter())

for node in leaves: 
    if node.taxon.label in mapping:
        new_node = Node(edge_length=node.edge_length)
        pNode = node.parent_node
        pNode.remove_child(node)
        pNode.add_child(new_node)
        new_node.add_child(node)
        pNode = new_node
        
        for taxon_name in mapping[node.taxon.label]:
            new_taxon = Taxon(label=taxon_name)
            myTree.taxon_namespace.add_taxon(new_taxon)
            new_node = Node(edge_length=0,taxon=new_taxon)
            pNode.add_child(new_node)



myTree.write_to_path(outfile,"newick")
