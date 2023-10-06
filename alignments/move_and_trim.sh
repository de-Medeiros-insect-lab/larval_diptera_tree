#get trim_alignments from Insect Egg Phylo github
conda activate mafft

mkdir -p aligned

for fasta_file in aligned_macse/*_NT.fasta
do
	    # get the base file name
	    base_name=$(basename "$fasta_file" _NT.fasta)

	    # copy the file to the aligned/ directory
	    cp "$fasta_file" aligned/${base_name}_aligned.fasta

	    # replace ! with - in the copied file in aligned/ directory
	    sed -i 's/!/-/g' "aligned/${base_name}_aligned.fasta"
done

for file in aligned_mafft/*.fasta; do 
    if [[ $(basename "$file") != *_refs_* ]]; then
        cp "$file" aligned/
    fi
done


for rRNA_align in 18S_aligned.fasta  28S_aligned.fasta
do
	python trim_alignments.py -a aligned/$rRNA_align --coverage 0.2 --min-data 100 --min-seqs 4	
done	

for CDS_align in 12S_16S_aligned.fasta AATS_aligned.fasta  CAD1_aligned.fasta  CAD2_aligned.fasta  COI_aligned.fasta  EF1a_aligned.fasta
do
	python trim_alignments.py -a aligned/$CDS_align --coverage 0.2 --min-data 100 --min-seqs 1
done

mkdir -p aligned_trimmed

mv aligned/*trimmed.fasta aligned_trimmed

# Remove reference sequences (starting with NW_ or NC_) from the aligned files
for file in aligned_trimmed/*.fasta; do
    awk '
    /^>/ {
        if ($0 ~ /^>NW_/ || $0 ~ /^>NC_/) {
            skip = 1;
        } else {
            skip = 0;
            print;
        }
        next;
    }
    {
        if (skip == 0) print;
    }
    ' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
done

# Replace >_R_ with > (mafft can add this)
sed -i 's/>_R_/>/g' aligned_trimmed/*.fasta

