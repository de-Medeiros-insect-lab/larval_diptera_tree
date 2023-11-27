iqtree -T 5 -s concatenated_alignment.nex -mset mrbayes -m MFP+MERGE -B 1000 -p partitions.nex -g partial_iqtree.tre --prefix Diptera_ML
iqtree -T 5 -s concatenated_alignment.nex -mset mrbayes -m MFP+MERGE -B 1000 -p partitions.nex --prefix Diptera_ML_unconstrained


