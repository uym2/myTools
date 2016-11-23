#! /usr/bin/env python

import sys

ssu_afa = sys.argv[1]
std_afa = sys.argv[2]

isFirst = True

with open(ssu_afa,'r') as fin:
	with open(std_afa,'w') as fout:
		for line in fin:
			if line[0] == '>':
				if not isFirst:			
					fout.write('\n')
				else:
					isFirst = False
				fout.write(line)
			else:
				fout.write(line[:-1])

