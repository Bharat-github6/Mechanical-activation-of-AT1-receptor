#!/bin/bash
for i in `seq 0 7`;
do
	sed 's/#.*//' ICL2$i.xvg > a.xvg
	sed 's/@.*//' a.xvg > a1.xvg
	awk '{print $1,$6,$7}' a1.xvg > a2.xvg
	awk 'FNR > 30 {print $1,$2,$3 }' a2.xvg > a6.xvg
	awk '{print$1, $2+$3}' a6.xvg > w$i.xvg
	awk 'FNR < 32012 {print $1,$2}' w$i.xvg > nw$i
	#awk '{print $1/(1)}' a6.xvg > a4.xvg
	#paste a4.xvg w$i.xvg > nw$i.xvg
done


cat nw* > a3.xvg
awk '{print $1, $2/(11)}' a3.xvg > a5.xvg
echo "#! FIELDS time ICL2" > combined_ICL2.txt 
sort -s -k1,1n a5.xvg >> combined_ICL2.txt

rm a*
rm nw*
rm w*



#paste w0.xvg w1.xvg w2.xvg w3.xvg w4.xvg w5.xvg w6.xvg w7.xvg > a3.xvg

#awk '{ print $1+$2+$3+$4+$5 }' a3.xvg > ICL.xvg
#rm a*


