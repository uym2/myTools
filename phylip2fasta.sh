#! /bin/bash

awk '{print ">"$1; print $2;}' $1 | tail -n+3 > $2
