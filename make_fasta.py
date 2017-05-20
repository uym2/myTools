#! /usr/bin/env python

from sys import argv,stdout

seq_file = argv[1]
taxname_file = argv[2]

if len(argv) > 3:
	fout = open(argv[3],'w')
else:
	fout = stdout

fs = open(seq_file,'r')
fn = open(taxname_file,'r')

for line in fn:
	fout.write(">"+line)
	fout.write(fs.readline())

fs.close()
fn.close()
if len(argv) > 3:
	fout.close()
