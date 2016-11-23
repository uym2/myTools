#! /usr/bin/env python
# usage: python count_sequence.py <filename>
import sys

filename = sys.argv[1]

count = 0

for line in open(filename,'r'):
	if line[0] == '>':
		count = count+1

print('sequence #: ', count)
