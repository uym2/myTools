#! /bin/bash

refTree=$1
cmpTree=$2

compareTrees $refTree $cmpTree | awk -F '\t' '{print $1,$3}' | numlist -fill; compareTrees $cmpTree $refTree | awk -F '\t' '{print $3,$1}' | numlist -miss1 | numlist -fill
