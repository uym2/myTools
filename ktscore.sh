#! /bin/bash

refTree=$1
cmpTree=$2

compareTrees.branches.sh $refTree $cmpTree | numlist -ktscore
