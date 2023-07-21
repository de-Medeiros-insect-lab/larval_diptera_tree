conda activate macse

mkdir -p aligned_macse
cd aligned_macse

echo -e "../to_align/AATS.fasta\n../to_align/CAD1.fasta\n../to_align/CAD2.fasta\n../to_align/EF1a.fasta" | parallel --progress --joblog ./NPC_macse.out.log --results ./ "macse -prog alignSequences -seq {} >> ./NPC_macse.out 2>&1"

