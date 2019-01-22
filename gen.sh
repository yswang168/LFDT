#! /bin/bash
# LPS="arabidopsis.lp budding.lp fission.lp mammalian.lp tcrNet.lp thelper.lp"
# To run
# $$0 logic.lp
LPS=$1
N=10
for lp in $LPS
do
DLP=${lp/.lp/}
if [ -d $DLP ]
then
   rm -fr $DLP
fi
mkdir $DLP
INS="10 20 40 80 160 320 640"
for I in $INS
do
  J=2
  while((J<=10))
  do
     K=1
     while ((K<=N))
     do
       python3.6 gen-lfdt.py lp/$lp $I $J > $DLP/$I-$J-$K 
       let K=K+1
     done
     let J=J+2 
  done
done
done
