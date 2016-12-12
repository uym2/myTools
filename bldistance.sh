#! /bin/bash

refTree=$1
cmpTree=$2

cmpTrees.allbr.sh $refTree $cmpTree | numlist -bld
