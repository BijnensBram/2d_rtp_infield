#!/bin/sh

for i in $(seq 0.6 0.1 1)
do
	./varyinga.exe 0.5 $i 0.01 500 2 > 6eright_$i.txt
	echo $i
done
echo "done"
