conda activate macse

mkdir -p aligned_macse
cd aligned_macse

echo -e "../to_align/COI.fasta" | parallel --progress --joblog ./COI_macse.out.log --results ./ "macse -prog alignSequences -seq {} >> ./COI_macse.out 2>&1"

mv ../to_align/*AA.fasta ../to_align/*NT.fasta ./

