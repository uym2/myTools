#!/usr/bin/env python
'''
Created on Jun 3, 2011

@author: smirarab

Modified on July 25, 2017
@author: uym2
'''

import dendropy
import sys
import os
import copy
import os.path

if __name__ == '__main__':

    if len(sys.argv) < 3: 
        print("USAGE: treefile output species_list")
        sys.exit(1)
    treeName = sys.argv[1]
    outputName = sys.argv[2]
    included = [s for s in sys.argv[3:]]
    #resultsFile="%s.%s" % (treeName, "renamed")
    trees = dendropy.TreeList.get_from_path(treeName, 'newick',preserve_underscores=True)
    filt = lambda node: True if (node.taxon is not None and node.taxon.label in included) else False
    
    for tree in trees:
        tree.filter_leaf_nodes(filt)

    trees.write(file=open(outputName,'w'), schema='newick', suppress_rooting=True)
