# larval_diptera_tree
Code and data used to create a tree to study larval Diptera evolution

# Step 1 - phylotar

folder phylotar

# Step 2 - manually choose one per genus

used phylotaR alingments, removed weird stuff

folder sequences/clean_sequences

# Step 3 - manually add additional taxa

folder sequences/seq_added

# Step 4 - alignments

folder alignments

MACSE for protein-coding
MAFFT for ribosomal and mitocondrial. 

Note: for rDNA, we noticed that alignments were very poor, apparently because unrelated regions were aligned. To mitigate this, we manually downloaded references sequences from genomes and mitogenomes encompassing all of the alignment region. We first BLASTED genomes in NCBI, downloaded the BLAST regions and also flanking regions. We then used Geneious to map all of the sequences in our alignment to this extract, refining the region of interest to the are that haf any sequences mapping. We finally went back to the genome in NCBI and used BLAST with the original the exact region as query to extract a fasta file containing only the region of interest.

Because we had these full-length references, we used a two-step approach for these aligments: we first aligned the reference sequences, and then we added the other sequences ussing --addfragments option in mafft.

# Step 5 - trimming and manual curation

After alignments, we lightly trimmed alignments removing flanking regions with few data points. For 18S and 28S, we also trimmed regions with fewer than 4 sequences in the middle of alignments. For the other genes, we manually trimmed the middle in multiples of 3 to avoid frame shifts.


# Phylogenetic constraints
The ultimate goal is to use these trees as family-level and genus-level constraints. 

Because tip names in phylogenies added as supplementary material are not standardized and often lack all relevant taxonomic information, the first step was to use a large language model (chatGPT v4) to assist in name parsing. the chat can be found here: https://chat.openai.com/share/13934687-d473-4eb6-8af3-4c7dedc836e5

Then, we manually checked the generated table for errors and used TaxReformer to pull additional data. 

With that information and manually rooted trees obtained from the primary sources, we were able to generate constraints. All steps are described in the  jupyter notebook: scripts/create_constraint.ipynb

For that, the first step is to translate the tip names into family names. We did this using chatGPT version 4. The full chat can be found in this link: 
