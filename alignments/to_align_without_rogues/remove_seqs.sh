#!/bin/bash

# Loop through each fasta file
for fasta in *.fasta; do
    # Use awk to process the file. If the sequence name after > is found in sequencesremoved.txt, skip the sequence and its corresponding data.
    awk 'BEGIN { RS=">"; FS="\n"; while(getline < "sequencesremoved.txt") seqs[$1]=1 }
    $1 && !($1 in seqs) { print ">"$0 }' "$fasta" > "$fasta.tmp"
    mv "$fasta.tmp" "$fasta"
done

