from=$1
to=$2
for i in `seq $from $to`; do cd job_$i; sbatch jobscr_$i.comet; cd ..; done

