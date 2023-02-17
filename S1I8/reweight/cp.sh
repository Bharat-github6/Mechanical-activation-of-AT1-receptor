

#!/bin/bash
for i in `seq 0 7`;
do
cp plumed.dat plumed$i.dat

echo "PRINT ARG=TM1_TM6,TM1_ICL2,TM5_ICL2,TM6_H8 FILE=colvar.$i" >>plumed$i.dat

done
