#iqtree -s concatenated_alignment.nex -m MFP+MERGE -B 1000 -p partitions.nex -T 5 -mset mrbayes --prefix Diptera_ML_unconstrained
iqtree -T 5 -s concatenated_alignment.nex -mset mrbayes -m MFP+MERGE -B 1000 -p partitions_simplified.nex -g partial_iqtree.tre -T AUTO --prefix Diptera_ML


