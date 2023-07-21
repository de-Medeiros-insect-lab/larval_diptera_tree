conda activate mafft

mkdir -p aligned_mafft
chmod 755 aligned_mafft

for file in to_align/12S_16S.fasta  to_align/18S.fasta  to_align/28S.fasta 
do
  name=$(basename "$file")
  echo $name
  mafft  --genafpair --maxiterate 10000 --thread -1 "$file" > "aligned_mafft/${name%.*}_aligned.fasta" 
done

