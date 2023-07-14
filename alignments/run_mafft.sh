conda activate mafft

mkdir -p aligned
chmod 755 aligned


for file in to_align/*.fasta
do
  name=$(basename "$file")
  echo $name
  mafft --genafpair --maxiterate 1000 --thread -1 "$file" > "aligned/${name%.*}_aligned.fasta" 
done

