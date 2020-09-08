#!/bin/sh

for i in $(seq 0 0.1 1)
do
	./infield_4rates.exe 1 $i 0.01 > a=$i.txt 
	echo $i
done

echo "done"
