#! /usr/bin/env python

from dendropy import TreeList
from sys import argv
from tree_lib import compute_diameter

infile = argv[1]

treelist = TreeList.get(path=infile,schema="newick")

compute_diameter(treelist)

