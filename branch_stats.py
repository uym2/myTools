#! /usr/bin/env python

import re
from dendropy import Tree
from sys import argv

filename = argv[1]

a_tree = Tree.get_from_path(filename,'newick')
br_sum = 0
br_count = 0
br_max = -1.0

for edge in a_tree.preorder_edge_iter():
	if edge.length is not None:
		br_count += 1
		br_sum += edge.length
		if edge.length > br_max:
			br_max = edge.length

br_avg = br_sum/br_count

print("branch #: " + str(br_count))
print("branch max: " + str(br_max))
print("branch sum: " + str(br_sum))
print("branch avg: " + str(br_avg))

