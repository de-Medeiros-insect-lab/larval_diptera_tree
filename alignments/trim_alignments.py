#!/usr/bin/env python

### Updated on 14-jul-23 by the user with the help of ChatGPT-4, an AI model developed by OpenAI

### The original script was created by Bruno de Medeiros on 03-jun-17, available at https://raw.githubusercontent.com/brunoasm/Insect_Egg_Phylogeny/master/trim_alignments.py 
### It was converted to Python 3 and streamlined to make the code more readable and efficient. 

### This script trims an alignment to the region with a given minimum coverage of ingroup taxa.
### It then removes sequences with more than 95% missing or ambiguous data.

### Updates included:
### - Converting the script to Python 3 from Python 2.
### - Replacing print statements with Python 3's print() function.
### - Replacing Python 2's xrange() with Python 3's range().
### - Streamlining several loops into single-line list comprehensions.
### - Replacing string concatenation with f-string formatting for better readability.
### - Changing pandas import to use the more common alias, pd.
### - Replacing iteritems() with items() for Python 3 dictionary iteration.
### - Removing unnecessary sys import.

import argparse
import pandas as pd
import dendropy
from collections import Counter
from os.path import basename, dirname

def detect_and_load_alignment(filepath, schema='fasta'):
    # Function to detect whether the input sequences are DNA or amino acids
    # and load them using the appropriate DendroPy class.
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('>'):
                continue  # Skip header lines
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            # Check if the line contains only DNA characters
            if all(char in 'ATCGNatcgn-' for char in line):
                return dendropy.DnaCharacterMatrix.get(path=filepath, schema=schema)
            else:
                return dendropy.ProteinCharacterMatrix.get(path=filepath, schema=schema)
    raise ValueError("Input file does not contain valid sequences.")


def get_ranges(indices):
    """Takes a sorted list of indices and returns a list of tuples,
    each representing a continuous range of indices."""
    ranges = []
    for i in indices:
        if ranges and i == ranges[-1][1] + 1:
            ranges[-1] = (ranges[-1][0], i)
        else:
            ranges.append((i, i))
    return ranges

def find_region_of_ingroup_high_coverage(alignment, outgroup_labels, minimum_coverage = 0.3, minimum_w_data=10):
    alignment = alignment.clone(2)
    out_taxa = [taxon for taxon in alignment.taxon_namespace if any([outgroup in taxon.label for outgroup in outgroup_labels])]
    alignment.remove_sequences(out_taxa)
    gapamb = ['-','N']

    idx_above_mincov = []
    idx_above_min_data = []
    nseqs = len(alignment.sequences())
    for i in range(alignment.sequence_size):
        temp_gapamb = sum(1 for seq in alignment.sequences() if str(seq[i]) in gapamb)

        if 1 - temp_gapamb / nseqs >= minimum_coverage:
            idx_above_mincov.append(i)
        if nseqs - temp_gapamb >= minimum_w_data:
            idx_above_min_data.append(i)

    start = min(idx_above_mincov)
    end = max(idx_above_mincov)
    idx = [i for i in idx_above_min_data if start <= i <= end]

    # Convert the lists of indices to lists of ranges for printing
    idx_above_mincov_ranges = get_ranges(sorted(idx_above_mincov))
    idx_above_min_data_ranges = get_ranges(sorted(idx_above_min_data))
    idx_ranges = get_ranges(sorted(idx))

    print(f"Coverage ranges kept: {idx_ranges}")
    print(f"Coverage ranges dropped: {list(set(idx_above_min_data_ranges) - set(idx_ranges))}")

    return idx


def number_not_missing(seq):
    counts = Counter(seq)
    not_missing = sum(counts[nuc] for nuc in ['A','C','T','G','R','Y','M','S','W','K'])
    return not_missing

def find_taxa_with_little_data(alignment, min_data = 100):
    taxa_to_drop = [taxon for taxon in alignment.taxon_namespace if number_not_missing(alignment[taxon].symbols_as_string()) < min_data]
    return taxa_to_drop

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--alignment', help = 'alignment in fasta format')
    parser.add_argument('-o','--outgroups', help = 'table with outgroup taxonomic ids for each clade')
    parser.add_argument('-c','--coverage', help = 'minimum coverage on the edge of alignments', default = 0.2)
    parser.add_argument('-m','--min-data', help = 'minimum number of non-missing nucleotides to keep a sample', default = 100)
    parser.add_argument('-s','--min-seqs', help  = 'minimum number of non-gap sequences to keep a position in the middle of the alignment', default = 10)
    parser.add_argument('-k','--keep-names', help = 'keep names as is. otherwise, we will remove _R_ added by mafft and any characters after the first space.', action = 'store_true')

    args = parser.parse_args()

    print('Trimming ' + args.alignment)

    all_outgroups = {}
    if args.outgroups:
        as_table = pd.read_csv(args.outgroups)
        all_outgroups = {x['higher_taxon']:str(x['ncbi_id']) for i,x in as_table.iterrows()}
    
    outgroup_labels = [x for i,x in all_outgroups.items() if i not in args.alignment]

    alignment = detect_and_load_alignment(args.alignment, schema='fasta')
    
    idx = find_region_of_ingroup_high_coverage(alignment, 
                                               outgroup_labels,
                                               minimum_coverage = float(args.coverage),
                                               minimum_w_data = int(args.min_seqs))
    
    new_alignment = alignment.export_character_indices(idx)

    taxa_to_drop = find_taxa_with_little_data(new_alignment, min_data = float(args.min_data))

    if taxa_to_drop:
        print(args.alignment)
        print('The following taxa were removed due to excess missing data:')
        print('\n'.join([taxon.label for taxon in taxa_to_drop]))
        new_alignment.remove_sequences(taxa_to_drop)

    if args.keep_names is not True:
        for taxon in new_alignment.taxon_namespace:
            if taxon.label.startswith('_R_'):
                taxon.label = taxon.label[3:]
            taxon.label = taxon.label.split(' ')[0]

        
    outpath = f'./{dirname(args.alignment)}/{basename(args.alignment).split(".")[0:-1]}_trimmed.fasta'
    with open(outpath, 'w') as outfile:
        new_alignment.write(file = outfile, schema = 'fasta')


