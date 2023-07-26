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


# Phylogeny tip name parsing
The ultimate goal is to use these trees as family-level constraints. For that, the first step is to translate the tip names into family names. We did this using chatGPT version 4. Here is an example of the prompt used:

~~~
User
Parse the tip names in the following phylogenetic tree to make a table including the following columns:
```tip_name,family,subfamily,genus,species,additional_identifiers``` 
Only use information explicitly contained in the tip names, filling missing data with NA. Output the table in a format to be copied and pasted to excel. Include only the table, no additional comments:
```
(Glossina_morsitans:0.12685192550801493994,((Mesembrina_meridiana:0.09920997026180304601,(Cordilura:0.08257045729495079978,(((Triarthria_setipennis:0.07814046713659697496,Pollenia:0.04382836459993738609)100:0.00829422272009596763,(Stomorhina_subapicalis:0.04706196481052474928,Calliphora_vomitoria:0.03380238423724006569)100:0.00555663790272519810)100:0.01023476912928669366,Sarcophaga_bullata:0.05468019021568650689)100:0.01733699621863537405)100:0.02143861999412616584)100:0.04230906651242698907,((((((Derocephalus_angusticollis:0.17433042912836096971,Micropeza_corrigiolata:0.13176482094531760669)100:0.02985352685541016460,(((Ceratitis_capitata:0.14107789233511380811,Zacompsia_fulva:0.11633105090805150039)100:0.03330108495264746948,Piophila_australis:0.12674020321389461996)100:0.01897823110155405849,((Strongylophthalmyia:0.15010527359338496356,(Meroplius_fasciculatus:0.18337046040994436913,Acartophthalmus_nigrinus:0.14164777845464304740)100:0.03665691079262803354)80:0.01057117090514482320,(Loxocera_cylindrica:0.18986755564382881700,Opomyza_germinationis:0.14570587303498164222)80:0.01462465807032054324)100:0.00922045928423191087)94:0.00610711183160734649)76:0.00542066064723189557,(((((Archimicrodon_brachycerus:0.21040449838947097860,Eristalis_pertinax:0.09936996134229024447)100:0.08949912551499882019,((Lonchoptera_bifurcata:0.24394220280512879384,(Megaselia_abdita:0.43571160918548296204,Platypeza_anthrax:0.18705594361660698999)100:0.03057051380791001721)100:0.03052424482508905509,(Meghyperus:0.20002934859086488051,(Hilarini:0.17170690034844263150,(Stilpon_pauciseta:0.29335501079604658914,Heteropsilopus_ingenuus:0.24470137062105742909)100:0.02455573938475860696)100:0.03904279818267399754)100:0.08533892535354137276)100:0.08785495960258940529)100:0.04218001308712131942,Nephrocerus_atrapilus:0.15031229247784153036)100:0.08405156481914707878,((Pseudodinia_antennalis:0.23444541168944016407,Stylogaster:0.24545454402527858151)100:0.01727498579729912914,((Helcomyza_mirabilis:0.07116564591516387484,Coelopa_frigida:0.07603617354125967454)91:0.00983063593401873985,(Sapromyza_sciomyzina:0.09855292065235887744,(Limnia_unguicornis:0.08079274650113991985,Myopa:0.17762136141994430694)100:0.02795361086709643311)42:0.00644785890671203260)100:0.01101309590208251338)100:0.02726941843895324194)100:0.03555446794179351749,((Leptocera_erythrocera:0.18464395060353624989,Diplogeomyza_tridens:0.08460318093403514095)100:0.01831988227839986133,Tapeigaster_digitata:0.09781884669546786482)100:0.01317982153766561471)100:0.00761945985331566236)74:0.00573739288224405820,((Syringogaster_plesioterga:0.15473251320668174325,Teleopsis_dalmanni:0.18320033588014325576)97:0.01562032023873908930,((Leiomyza_laevigata:0.21440966573966477315,Mumetopia_occipitalis:0.17048777990433175433)80:0.01512349296578317098,(Australimyza_mcalpinei:0.19385020578294803739,Dasyrhicnoessa_insularis:0.18167694596677344543)80:0.02418936350651241379)100:0.00996519688074707158)69:0.00695794625573405850)87:0.00682507927413178277,((Nemo_dayi:0.11874738530426584560,Lipara_lucens:0.18267038607792979166)100:0.04979781804172350029,((Scutops:0.26533766879771042424,Aulacigaster_mcalpinei:0.23280351524062148361)97:0.02095282271248671488,((Fergusonina_omlandi:0.29946515416296404233,Carnus_hemapterus:0.22678635373950872811)100:0.03075031002983729528,(Odinia_conspicua:0.20193362555746469100,Melanagromyza:0.26173526433112315193)100:0.02399044428706543358)99:0.01076076448077288063)80:0.00726980262300032983)93:0.00794226257620269521)100:0.01185566449410392457,(Scatella_tenuicosta:0.21378626867418867863,((Curtonotum:0.13434114995631171730,Diastata_repleta:0.11930926661680889278)100:0.01391086521218228012,(Cryptochetum:0.57398137547189809204,((((D_busckii:0.09007939097974269893,D_virilis:0.05781521941240004570)100:0.03463132904402183021,Drosophila_melanogaster:0.11163772915468063440)100:0.03255114890365541636,Chymomyza_costata:0.09268277881275728547)100:0.09518748214006760022,(Braula_coeca:0.16624385689913903641,(Phortica_variegata:0.09435009028765807548,Stegana:0.11646831362579732061)100:0.01842060160299545390)100:0.02175280044339161778)92:0.01725879578831809175)100:0.02804913766379295292)100:0.04579182717595477181)100:0.01571884298958411627)100:0.08165465053896517333)100:0.05348111505449681252,Ortholfersia_macleayi:0.24882651197951138888);
```
~~~
