#! /usr/bin/env python

# usage: python print_taxa.py <treefile> <listing=0|1> <counting=0|1>

from tree_lib import report_taxa
from sys import argv

arg_count = len(argv)

opts = {'listing':1,'counting':1}
pos_resp=['1','true','True','T']

if arg_count > 2:
	(k,v) = argv[2].split('=')
	opts[k] = (v in pos_resp)	
if arg_count > 3:
	(k,v) = argv[3].split('=')
	opts[k] = (v in pos_resp)	

report_taxa(argv[1],listing=opts['listing'],counting=opts['counting'])
