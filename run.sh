#!/bin/sh

for i in 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0
do
	# ./infield_4rates.exe 0.5 $i 0.01 500 1 > left_$i.txt 
	./infield_4rates.exe 0.5 $i 0.01 500 2 > 2new_right_$i.txt 
	# ./infield_4rates.exe 0.5 $i 0.01 500 3 > sym_$i.txt 
	echo $i
done
echo "done"
