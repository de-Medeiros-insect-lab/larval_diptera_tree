#!/bin/bash

# Make sure the output directory exists
mkdir -p ./to_align

# Get list of unique gene names (base filenames without extension)
genes=$(find ../sequences/ -name '*.fasta' | xargs -n 1 basename | cut -d . -f 1 | sort | uniq)

# Loop over each unique gene name
for gene in $genes
do
    echo $gene
    # Find all fasta files for the gene
    files=$(find ../sequences/ -name "${gene}*.fasta")
    echo $files
    
    # Create a temporary file for concatenation
    tmp_file="./to_align/${gene}_tmp.fasta"
    
    # Empty the temporary file
    > "$tmp_file"

    # Loop over each file
    for file in $files
    do
        # Use awk to ensure newline at the end of the file and to remove everything in the sequence names starting with "|"
        # Also remove spaces from sequence names
        awk 'END{print ""} {gsub(/\|.*$/, ""); gsub(/ /, ""); print}' "$file" >> "$tmp_file"
    done

    # Rename the temporary file
    mv "$tmp_file" "./to_align/${gene}.fasta"
done

