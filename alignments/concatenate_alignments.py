import dendropy
import os

# Directory containing the FASTA files
directory = "."

# Order of the genes in the final alignment
gene_order = [
    "12S_16S", "18S", "28S", "AATS", "EF1a", "CAD1", "CAD2", "COI"
]

# Initialize a TaxonNamespace object
taxon_namespace = dendropy.TaxonNamespace()

# Create a unified list of all taxa across all genes
all_taxa = set()
for gene in gene_order:
    file_path = os.path.join(directory, f"{gene}_aligned_trimmed_clean.fasta")
    temp_alignment = dendropy.DnaCharacterMatrix.get(
        path=file_path,
        schema="fasta"
    )
    for taxon in temp_alignment.taxon_namespace:
        all_taxa.add(taxon.label)

# Update the taxon_namespace with all taxa
for taxon in all_taxa:
    taxon_namespace.new_taxon(taxon)

# Initialize a list to store all gene alignments
gene_alignments = []

# Initialize a dictionary for partition ranges
partition_ranges = {}
current_position = 1

# Process each gene
for gene in gene_order:
    file_path = os.path.join(directory, f"{gene}_aligned_trimmed_clean.fasta")
    
    # Read the alignment
    alignment = dendropy.DnaCharacterMatrix.get(
        path=file_path,
        schema="fasta",
        taxon_namespace=taxon_namespace
    )

    # Ensure alignment includes sequences for all taxa
    for taxon in taxon_namespace:
        if taxon.label not in alignment:
            alignment.new_sequence(taxon, "?" * alignment.sequence_size)

    gene_alignments.append(alignment)

    # Record the partition range for this gene
    gene_length = alignment.sequence_size
    partition_ranges[gene] = (current_position, current_position + gene_length - 1)
    current_position += gene_length

# Concatenate the alignments
concatenated_alignment = dendropy.DnaCharacterMatrix.concatenate(gene_alignments)

# Write the concatenated alignment to a Nexus file
concatenated_file_path = os.path.join(directory, "concatenated_alignment.nex")
concatenated_alignment.write(
    path=concatenated_file_path,
    schema="nexus"
)

# Write the partition file
partition_file_path = os.path.join(directory, "partition_file.nex")
with open(partition_file_path, "w") as partition_file:
    partition_file.write("#nexus\nbegin sets;\n")
    
    for gene, (start, end) in partition_ranges.items():
        if gene in ["AATS", "EF1a", "CAD1", "CAD2", "COI"]:  # protein-coding genes
            for i in range(3):
                partition_file.write(f"    charset {gene}_{i + 1} = {start + i}-{end}\\3;\n")
        else:
            partition_file.write(f"    charset {gene} = {start}-{end};\n")
    
    partition_file.write("end;")

# Output paths for confirmation
print(f"Concatenated alignment saved to: {concatenated_file_path}")
print(f"Partition file saved to: {partition_file_path}")

