#! /usr/bin/env python

import re
from sys import argv

filename = argv[1]

pattern = re.compile(r"\:[0-9]+(?:\.[0-9]+)?")

with open(filename,'r') as f:
	tree = f.readlines()

br_len = [float(x[1:]) for x in pattern.findall(tree[0])]

br_count = len(br_len)
br_sum = sum(br_len)
br_avg = br_sum/br_count

print "branch #: " + str(br_count)
print "branch sum: " + str(br_sum)
print "branch avg: " + str(br_avg)

