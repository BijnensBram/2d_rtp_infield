#!/bin/sh

for i in 4.0 5.0
do
	# ./infield_4rates.exe 0.5 $i 0.01 500 1 > left_$i.txt 
	./infield_4rates.exe $i 0.5 0.01 500 2 > 3c_right_$i.txt 
	# ./infield_4rates.exe 0.5 $i 0.01 500 3 > sym_$i.txt 
	echo $i
done
echo "done"
