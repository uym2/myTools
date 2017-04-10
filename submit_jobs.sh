from=$1
to=$2
device=$3
for i in `seq $from $to`; do cd job_$i; sbatch jobscr_$i\.$device; cd ..; done

