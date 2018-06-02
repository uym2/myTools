# !/bin/bash

tre1=$1
tre2=$2

tre1_induced=`mktemp`
tre2_induced=`mktemp`

#filter_taxon_from_tree.py $tre1 $tre1_induced `nw_labels $tre2`
#filter_taxon_from_tree.py $tre2 $tre2_induced `nw_labels $tre1`

echo "pruning tree1 ..."
prune_tree.py -i $tre1 -o $tre1_induced -l "`nw_labels -I $tre2`" -v

echo "pruning tree2 ..."
prune_tree.py -i $tre2 -o $tre2_induced -l "`nw_labels -I $tre1`" -v

echo "comparing the induced trees ..."
dRF_norm.sh $tre1_induced $tre2_induced

rm $tre1_induced $tre2_induced
