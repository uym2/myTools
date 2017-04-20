#! /bin/bash

taskfile=$1
nj=$2 # number of jobs per splitted taskfile
np=$3 # number of processors per job
ncore=$4 # number of cores per node
jobname=$5
queue=$6

i=1;
j=1;

curr_file=`mktemp task-XXXXX`

while read line; do
	echo $line >> $curr_file
	if [ $j -lt $nj ]; then
		j=$((j+1))
	else
		mkdir job\_$i
		mv $curr_file job\_$i/task$i
		cp /home/umai/my_gits/myTools/jobscr_template.comet job\_$i/jobscr_$i.comet
		sed -i "s/#####/$jobname/g" job\_$i/jobscr_$i.comet
		sed -i "s/%%%%%/$queue/g" job\_$i/jobscr_$i.comet
		sed -i "s/@@@@@/$ncore/g" job\_$i/jobscr_$i.comet
		echo python /home/umai/my_gits/myTools/core_launcher.py task$i $np >> job\_$i/jobscr_$i.comet
		j=1
		i=$((i+1))
		curr_file=`mktemp task-XXXXX`
	fi
done < $taskfile

if [ -s $curr_file ]; then
	mkdir job\_$i
	mv $curr_file job\_$i/task$i
	cp /home/umai/my_gits/myTools/jobscr_template.comet job\_$i/jobscr_$i.comet
	sed -i "s/#####/$jobname/g" job\_$i/jobscr_$i.comet
	sed -i "s/%%%%%/$queue/g" job\_$i/jobscr_$i.comet
	sed -i "s/*****/$ncore/g" job\_$i/jobscr_$i.comet
	echo python /home/umai/my_gits/myTools/core_launcher.py task$i $np >> job\_$i/jobscr_$i.comet
else
	rm $curr_file
fi
