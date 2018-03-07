#! /bin/bash

infile=$1
outfile=$2

seq_names=`grep ">" $infile | sed "s/>//g" | sort | uniq`

sample_from_seq_names.py $infile $outfile $seq_names
