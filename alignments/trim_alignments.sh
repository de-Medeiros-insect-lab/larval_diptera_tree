#get trim_alignments from Insect Egg Phylo github
conda activate mafft

for rRNA_align in 12S_16S_aligned.fasta  18S_aligned.fasta  28S_aligned.fasta
do
	python trim_alignments.py -a aligned/$rRNA_align --coverage 0.2 --min-data 100 --min-seqs 4	
done	

for CDS_align in  AATS_aligned.fasta  CAD1_aligned.fasta  CAD2_aligned.fasta  COI_aligned.fasta  EF1a_aligned.fasta
do
	python trim_alignments.py -a aligned/$CDS_align --coverage 0.2 --min-data 100 --min-seqs 1
done

mkdir -p aligned_trimmed

mv aligned/*trimmed.fasta aligned_trimmed
