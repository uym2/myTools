#! /usr/bin/env python

# sample a tree with specified number of ingroups and outgroups

from tree_lib import sample_with_outgroups, prune_tree
from sys import argv, stdout
from dendropy import Tree
import argparse
from os.path import splitext, abspath

parser = argparse.ArgumentParser()

parser.add_argument("-t","--tree",required=True,help="Input tree")
parser.add_argument("-i","--ingroups",required=True,help="Number of ingroup species")
parser.add_argument("-o","--outgroups",required=False,help="Number of outgroup species. Default:1")
parser.add_argument("-r","--replicates",required=False,help="Number of replicates. Default: 1")
parser.add_argument("-e","--outtree",required=False,help="Where to write the output trees to. Default: Inferred from the name of the input tree")
parser.add_argument("-f","--outfile",required=False,help="Where to write the ingroups/outgroups of the samples to. Default: print to screen")
parser.add_argument("-p","--pruneOG",required=False,help="Prune the outgroups and write the pruned tree to this file. Default: skip this")

args = vars(parser.parse_args())

treefile = args["tree"]
n_ingroups = int(args["ingroups"])
n_outgroups = int(args["outgroups"]) if args["outgroups"] else 1
n_reps = int(args["replicates"]) if args["replicates"] else 1

base_name,ext = splitext(treefile)
outtreeFile = args["outtree"] if args["outtree"] else (base_name + "_sampled.trees")
outfile = args["outfile"]
outtree_noOG = args["pruneOG"]

tree = Tree.get_from_path(treefile,'newick')
ID = 0

check,samples = sample_with_outgroups(tree, n_ingroups, n_outgroups=n_outgroups, n_reps=n_reps)

if not check:
    print("The tree is not large enough for this sampling size!")
else:
    if outfile:
        fout_info = open(outfile,'w')
    else:
        fout_info = stdout

    fout_info.write("Sampled from " + abspath(treefile) + "\n")
    fout_info.write("Sampled " + str(n_reps) + " replicate(s) of " + str(n_ingroups) + " ingroup(s) and " + str(n_outgroups) + " outgroup(s)\n")
    with open(outtreeFile,'w') as fout_tree:
        for i,(t,igs,ogs) in enumerate(samples):
            fout_info.write("Rep " + str(i+1)+":\n")
            fout_info.write("Ingroups: ")
            for i in igs:
                fout_info.write(i + " ")
            fout_info.write("\nOutgroups: ")
            for o in ogs:
                fout_info.write(o + " ")
            fout_info.write("\n")
            fout_tree.write(t.as_string('newick'))

    fout_info.close()

    if outtree_noOG:
        with open(outtree_noOG,'w') as f:
            for t,igs,ogs in samples:
                prune_tree(t,ogs)
                f.write(t.as_string('newick'))                

