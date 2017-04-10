#! /usr/bin/env python

from dendropy import TreeList
from sys import argv

trees = TreeList()
trees.read(path=argv[1],schema="newick")

trees.write(path=argv[2],schema="nexus")
