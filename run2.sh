#!/bin/sh

for i in $(seq 0.4 0.2 0.8)
do
	# ./infield_4rates.exe 0.5 $i 0.01 500 1 > left_$i.txt 
	./infield_4rates.exe 0.5 $i 0.01 500 2 > right_$i.txt 
	# ./infield_4rates.exe 0.5 $i 0.01 500 3 > sym_$i.txt 
	echo $i
done
echo "done"
