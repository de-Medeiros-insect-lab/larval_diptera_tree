conda activate macse

mkdir -p aligned_macse
cd aligned_macse

echo -e "../to_align_without_rogues/COI.fasta" | parallel --progress --joblog ./COI_macse.out.log --results ./ "macse -prog alignSequences -gc_def 5 -seq {} >> ./COI_macse.out 2>&1"

mv ../to_align_without_rogues/*AA.fasta ../to_align_without_rogues/*NT.fasta ./

