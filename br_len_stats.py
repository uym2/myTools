#! /usr/bin/env python

import re
from sys import argv

filename = argv[1]

pattern = re.compile(r"\:[0-9]+(?:\.[0-9]+)?")

with open(filename,'r') as f:
	tree = f.readlines()

#print pattern.findall(str[0])
br_len = [float(x[1:]) for x in pattern.findall(tree[0])]

br_count = len(br_len)
br_avg = sum(br_len)/br_count

#print br_count
#print br_avg

print "branch #: " + str(br_count)
print "branch avg: " + str(br_avg)

