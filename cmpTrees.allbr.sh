#! /bin/bash

refTree=$1
cmpTree=$2

compareTrees.leaf_include $refTree $cmpTree | awk -F '\t' '{print $1,$3}' | tail -n +2 | numlist -fill ; compareTrees $cmpTree $refTree | awk -F '\t' '{print $3,$1}' | tail -n +2 | numlist -miss1 | numlist -fill
