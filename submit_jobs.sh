from=$1
to=$2
machine=$3

if [ $machine == 'comet' ]; then 
	for i in `seq $from $to`; do cd job_$i; sbatch jobscr_$i.comet; cd ..; done
elif [ $machine == 'tscc' ]; then
	for i in `seq $from $to`; do cd job_$i; qsub jobscr_$i.tscc; cd ..; done
fi
