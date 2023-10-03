conda activate macse

mkdir -p aligned_macse
cd aligned_macse

echo -e "../to_align_without_rogues/AATS.fasta\n../to_align_without_rogues/CAD1.fasta\n../to_align_without_rogues/CAD2.fasta\n../to_align_without_rogues/EF1a.fasta" | parallel --progress --joblog ./NPC_macse.out.log --results ./ "macse -prog alignSequences -seq {} >> ./NPC_macse.out 2>&1"

