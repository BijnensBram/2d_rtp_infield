#!/bin/sh

# for i in $(seq 0 0.1 1)
# do
# 	# ./infield_4rates.exe $i 1 0.01 > neg_c=$i.txt 
# 	# ./passive.exe $i 1 0.01 > neg_passive_c=$i.txt 
# 	# ./4rates.exe $i 1 0.01 > noa=$i.txt 
# 	./infield_4rates.exe 0 1 0.01 > neg_c=$i.txt 
# 	echo $i
# done

# echo "done"
for i in $(seq 0.5 0.5 1.5)
do
	./infield_4rates.exe $i 10 0.01 > neg_c=$i.txt 
	# ./4rates.exe $i 1 0.01 > neg_c=$i.txt 
	# ./passive.exe $i 1 0.01 > neg_passive_c=$i.txt 
	# ./4rates.exe $i 1 0.01 > noa=$i.txt 
	# ./4rates.exe 0 1 0.01 > traject$i.txt 
	echo $i
done
echo "done"
