#! /bin/bash

intree=$1
count=$2
outtree=$3

taxafile=`mktemp`

if [ ! $count -eq 0 ]; then
 	nw_labels -I $intree > $taxafile
 	nw_prune $intree `subsample.py $taxafile $count` > $outtree
else
 	cp $intree $outtree
fi

rm $taxafile      
