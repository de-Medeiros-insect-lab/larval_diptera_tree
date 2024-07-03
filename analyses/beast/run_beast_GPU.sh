conda activate beast2
export LD_LIBRARY_PATH=/home/bdemedeiros/software/miniconda3/envs/beast2/lib:$LD_LIBRARY_PATH
#./beast/bin/beast -overwrite -statefile checkpoint -beagle_GPU -beagle_single -beagle_order 2,1,2,3,1,4,3,4 -seed 45684121 Diptera_with_rogues.xml
#./beast/bin/beast -resume -statefile checkpoint -beagle_GPU -beagle_single -beagle_order 2,1,2,3,1,4,3,4 -seed 45684121 Diptera_with_rogues.xml

./beast/bin/beast -overwrite -statefile checkpoint -beagle_GPU -beagle_single -beagle_order 2,1,2,1,1,2,1,2 -seed 45684121 Diptera_with_rogues_and_hard_constraints.xml
#./beast/bin/beast -resume -statefile checkpoint -beagle_GPU -beagle_single -beagle_order 2,1,2,3,1,4,3,4 -seed 45684121 Diptera_with_rogues.xml
