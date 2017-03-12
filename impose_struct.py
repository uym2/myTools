#! /usr/bin/env python

from sequence_lib import impose_struct
from sys import argv

f1 = open(argv[1],'r')
f2 = open(argv[2],'r')

seq = f1.readlines()
struct = f2.readlines()

impose_seq = ''
impose_str = ''

fout = open(argv[3],'w')
for i,s in enumerate(seq):
	seq1,str1 = impose_struct(s.rstrip(),struct[i].rstrip())
	impose_seq += seq1
	impose_str += str1

fout.write(impose_seq+'\n')
fout.write(impose_str+'\n')
fout.close()
