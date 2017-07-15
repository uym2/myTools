#! /bin/bash

infile=$1
samplefile=$2
outfile=$3

sample_from_seq_names.py $infile $outfile `get_seq_names.sh $samplefile`

