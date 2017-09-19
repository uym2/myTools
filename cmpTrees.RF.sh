# !/bin/bash

tre1=$1
tre2=$2

tre1_induced=`mktemp`
tre2_induced=`mktemp`

filter_taxon_from_tree.py $tre1 $tre1_induced `nw_labels $tre2`
filter_taxon_from_tree.py $tre2 $tre2_induced `nw_labels $tre1`

dRF_norm.sh $tre1_induced $tre2_induced

rm $tre1_induced $tre2_induced
