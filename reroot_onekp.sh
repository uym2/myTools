#!/bin/sh
reroot.py $1 Monomastix_opisthostigma+Uronema_sp+Nephroselmis_pyriformis+Pyramimonas_parkeae,Chlorokybus_atmophyticus+Spirotaenia_minuta+Mesostigma_viride,Entransia_fimbriata+Klebsormidium_subtile -mrca $2

if [ ! -s $2 ]; then 
	echo "Rerooting using midpoint ..." 
	FastRoot.py -i $1 -o $2 -m MP
fi
