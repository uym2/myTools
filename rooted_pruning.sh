#! /bin/bash

a_tree=$1
k=$2
outtree=$3

mean=`nw_distance $a_tree | numlist -avg`
sd=`nw_distance $a_tree | numlist -std` # terrible solution!
thres=`echo $mean+$sd*$k | bc`
prune_by_threshold.py $a_tree $thres $outtree
