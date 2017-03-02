# !/usr/bin/env python

from sequence_lib import is_aligned
from sys import argv

if is_aligned(argv[1]):
	print("Aligned")
else:
	print("Not aligned")
