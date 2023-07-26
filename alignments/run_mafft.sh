conda activate mafft

mkdir -p aligned_mafft
chmod 755 aligned_mafft

for gene in 12S_16S 18S 28S 
do
  echo $gene
  mafft --genafpair --adjustdirectionaccurately --thread -1 "to_align/${gene}_refs.fasta" > "aligned_mafft/${gene}_refs_aligned.fasta"
  mafft  --genafpair --multipair --adjustdirectionaccurately --addfragments to_align/${gene}.fasta --thread -1 "aligned_mafft/${gene}_refs_aligned.fasta" > "aligned_mafft/${gene}_aligned.fasta"
done
