#! /usr/bin/env python

from tree_lib import prune_node
from dendropy import Tree
import argparse
from random import shuffle
from os.path import basename, dirname, splitext,realpath,join,normpath,isdir,isfile,exists
from os import mkdir

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input",required=True,help="Input tree")
parser.add_argument("-o","--output",required=True,help="Output directory")
parser.add_argument("-n","--nleaves",required=True,help="Size of each subtree. Can be a list or a number")
parser.add_argument("-r","--rep",required=False,help="Number of replicates. Default: 1")

args = vars(parser.parse_args())

def get_leaf_list(tree):
    leaves = []
    for node in tree.leaf_node_iter():
        leaves.append(node)
    return leaves

def shuffle_and_prune(tree,nleaves):
# assume nleaves is sorted in descending order    
    tree_rep = Tree.get(data = tree.as_string(schema='newick'),schema='newick')  
    leaves = get_leaf_list(tree_rep)
    shuffle(leaves)
    N = len(leaves)
    curr_idx = 0
    treeList = []

    for n in nleaves:  
        x = N-n
        while curr_idx < x:
            prune_node(tree_rep,leaves[curr_idx])
            curr_idx += 1
        treeList.append(tree_rep.as_string('newick'))
    
    return treeList    

inFile = args["input"]
outdir = args["output"]
nleaves = [int(n) for n in args["nleaves"].split()]
nleaves.sort(reverse=True)
nrep = int(args["rep"]) if args["rep"] else 1

tree = Tree.get_from_path(inFile,'newick')

# make outdir and a sub-directory for each desired subtree's size
mkdir(outdir)
for n in nleaves:
    dirName = normpath(join(outdir,str(n))) 
    mkdir(dirName)

ndigits = len(str(nrep))+1

for r in range(nrep):
    print("Producing replicate " + str(r+1))
    treeList = shuffle_and_prune(tree,nleaves)
    for (n,t) in zip(nleaves,treeList):
        treefile = normpath(join(outdir,str(n),"rep_"+str(r+1).rjust(ndigits,'0')+".tre"))
        with open(treefile,'w') as fout:
            fout.write(t)
    

                
