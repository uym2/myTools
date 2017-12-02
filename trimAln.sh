#! /bin/bash

infile=$1 # fasta format
outfile=$2 # fasta format
bp=$3 # the number of basepairs to be trimmed. Note that $bp must be at most the size of $infile

sed -e "s/>\(.*\)/@>\1@/g" $infile | tr -d "\n"|tr "@" "\n"|tail -n+2|awk '{print substr($1,0,'$bp')}' > $outfile  
