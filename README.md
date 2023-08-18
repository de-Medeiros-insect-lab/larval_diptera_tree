# larval_diptera_tree
Code and data used to create a tree to study larval Diptera evolution.

The goal is to use as much data as available on gene bank for genus-level relationships and combine with the best available phylogenetic knowledge in the form of constraints.

# Step 1 - phylotar

We used phylotaR to retrieve the initial dataset. See folder phylotaR for options and scripts. Briefly, we kept all phylotaR clusters that were shared for a good number of Diptera genera and tentatively named these clusters based on common terms for these sequences in NCBI

# Step 2 - manually choose one per genus

Using phylotaR tools, we kept up to 3 sequences per genus (the 3 longest). We then did initial alignments and manually selected one sequence per genus that seemed to have the best alignment to other sequences. The results are saved in folder sequences/clean_sequences

# Step 3 - manually add additional taxa

Because we continued phenotyping larvae after the original phylotaR dataset, we manually used BLAST on gene bank to enrich our datasets for additional taxa. We did not increase the number of genes. Additional sequences are found in folder sequences/seq_added

# Step 4 - alignments

folder alignments

MACSE for protein-coding
MAFFT for ribosomal and mitocondrial. 

Note: for rDNA, we noticed that alignments were very poor, apparently because unrelated regions were aligned. To mitigate this, we manually downloaded references sequences from genomes and mitogenomes encompassing all of the alignment region. We first BLASTED genomes in NCBI, downloaded the BLAST regions and also flanking regions. We then used Geneious to map all of the sequences in our alignment to this extract, refining the region of interest to the are that haf any sequences mapping. We finally went back to the genome in NCBI and used BLAST with the original the exact region as query to extract a fasta file containing only the region of interest.

Because we had these full-length references, we used a two-step approach for these aligments: we first aligned the reference sequences, and then we added the other sequences ussing --addfragments option in mafft.

# Step 5 - trimming and manual curation

After alignments, we lightly trimmed alignments removing flanking regions with few data points. For 18S and 28S, we also trimmed regions with fewer than 4 sequences in the middle of alignments. For the other genes, we manually trimmed the middle in multiples of 3 to avoid frame shifts.

# Step 6 - concatenate alignments

We used phyutility to concatenate alignments and export in nexus format. We then manually edited the comments in this nexus file generated by phyutility to generate a partition file for IQTREE. For the 12S_16S cluster, we additionally used Geneious to annotate the alignments and identify coding and noncoding regions (this cluster included from 12S to cytb).
Final alignment and its concatenated version are saved in folder alignments/alignments_trimmed_cleaned

# Step 7 -  Phylogenetic constraints
We used the trees listed in folder constraint_trees to generate phylogenetic constraints.

Because tip names in phylogenies added as supplementary material are not standardized and often lack all relevant taxonomic information, the first step was to use a large language model (chatGPT v4) to assist in name parsing. the chat can be found here: https://chat.openai.com/share/13934687-d473-4eb6-8af3-4c7dedc836e5

Then, we manually checked the generated table for errors and used TaxReformer to pull additional data. 

With that information and manually rooted trees obtained from the primary sources, we were able to generate constraints. All steps are described in the  jupyter notebook: scripts/create_constraint.ipynb

# Step 8 - Maximum likelihood tree
We copied the concatenated alignment, phylogenetic constraints and made an IQTREE partition file in the folder analyses/IQTREE. It also constains the bash script that calls IQTREE with all options.

# Step 9 - unconstrained maximum likelihood tree
We got an error of negative branch length when running Step 8. Therefore, we ran an unconstrained ML tree to find taxa that may be mislabelled/misplaced (such as NUMT copies).

We manually noted samples that seemed misplaced based on superfamily clusters. From these, we decided to exclude samples that (1) had sequence information from only 1 gene AND (2) had bootstrap values >50. These samples were excluded from the constraint tree and concatenated sequence files.

# Step 10 - rerun maximum likelihood tree