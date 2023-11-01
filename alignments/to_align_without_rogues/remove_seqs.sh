#!/bin/bash

# File containing the list of sequences to be removed
sequences_removed_file="sequencesremoved.txt"

# Directory containing the FASTA files
fasta_dir="."

# Read the list of sequences to be removed into an array
sequences_to_remove=()
while IFS= read -r line; do
  sequences_to_remove+=("$line")
done < "$sequences_removed_file"

# Function to check if an array contains a value
contains_element () {
  local element match="$1"
  shift
  for element; do
    [[ "$element" == "$match" ]] && return 0
  done
  return 1
}

# Process each FASTA file
for fasta_file in "$fasta_dir"/*.fasta; do
  echo "Processing $fasta_file..."
  
  # Temporary file to store sequences to be kept
  temp_file=$(mktemp)
  
  # Variable to keep track of whether to write the current sequence
  write_sequence=false
  
  while IFS= read -r line; do
    if [[ "$line" == ">"* ]]; then
      sequence_id="${line#>}"
      if contains_element "$sequence_id" "${sequences_to_remove[@]}"; then
        write_sequence=false
      else
        write_sequence=true
      fi
    fi
    
    if [ "$write_sequence" = true ]; then
      echo "$line" >> "$temp_file"
    fi
  done < "$fasta_file"
  
  # Replace the original FASTA file with the temporary file
  mv "$temp_file" "$fasta_file"
done

echo "Done."

