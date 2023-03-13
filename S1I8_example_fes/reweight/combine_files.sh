#!/bin/bash

echo "#! FIELDS time xi" > combined_cv.txt
for i in `seq 0 7`
do
    mdir=M`printf "%03d" $i`
    grep -v "#" ../$mdir/colvar.$i | awk '{print $1,$4}' >> tmp1
done
sort -s -k1,1n tmp1 >> combined_cv.txt
rm tmp1
