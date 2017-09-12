#! /bin/bash

infile=$1

grep ">" $infile | sed "s/>//g" | tr "\n" " "
