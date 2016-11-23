#! /usr/bin/env python

import sys

filename = sys.argv[1]

maxlength = 0
currlength = 0

with open(filename,'r') as f:
	for line in f:
		if line[0] == '>':
			if maxlength < currlength:
				maxlength = currlength
			currlength = 0
		else:
			currlength = currlength + len(line)-1

print maxlength		
