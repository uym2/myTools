#! /usr/bin/env python

# remove leaves that are distant more than a given threshold from the root
# only works for rooted tree

from dendropy import Tree
from sys import argv,stdout

def filter_by_threshold(a_tree,threshold):
    def __filter(node,cumm_l):
        removed = False
        node.child_removed = False
        for child in node.child_nodes():
            check = __filter(child,cumm_l + child.edge_length)
            removed = removed or check
        
        p = node.parent_node
        #if ( cumm_l > threshold ) or ( node.child_removed and len(node.child_nodes()) == 0 ):
        if ( cumm_l > threshold ) or ( node.child_removed and node.num_child_nodes() == 0 ):
            # remove node
            p.remove_child(node)
            # update parent node
            p.child_removed = True
            removed = True
            if node.taxon:
                print(node.taxon.label)
            #except:
            #    print(node.label + " removed")
        #elif len(node.child_nodes()) == 1:
        elif node.num_child_nodes() == 1:
            if node is a_tree.seed_node:
                a_tree.seed_node = node.child_nodes()[0]
            else:
                # remove node and attach its only child to its parent
                e1 = node.edge_length
                child = node.child_nodes()[0]
                e2 = child.edge_length
                p.remove_child(node)
                node.remove_child(child)
                p.add_child(child)
                child.edge_length = e1 + e2
        return removed  
    
    return __filter(a_tree.seed_node,0)         

infile = argv[1]
thres = float(argv[2])
outfile = argv[3]

a_tree = Tree.get_from_path(infile,"newick",preserve_underscores=True)
filter_by_threshold(a_tree,thres)
a_tree.write_to_path(outfile,"newick")
