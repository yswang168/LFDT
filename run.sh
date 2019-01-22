#! /bin/bash
# Run LFDT to learn logic program from state transitions
# LPS="arabidopsis.lp budding.lp fission.lp mammalian.lp tcrNet.lp thelper.lp"
# To run
# $$0 [options] instance-class 
# instance_class: arabidopsis|budding|fission|mammalian|tcrNet|thelper
# options: 
# -n: nonrecursive
# -c: no combined resolution
# -g: no ground resolution
# -q: don't print learned rules
# -f: save the learned logic programs into llp/instance_class
# By Yisong wang 
# 2018.12.10
function usage(){
  echo "usage: $0 [options] [-l <instance-class>]"
  echo "instance_class: arabidopsis|budding|fission|mammalian|tcrNet|thelper"
  echo "options:"
  echo "-n: nonrecursive"
  echo "-c: no combined resolution"
  echo "-g: no ground resolution"
  echo "-q: don't print learned rules"
  echo "-f: save the learned logic programs into llp/instance_class"
  echo "-l <instance-class> (default is budding)"
  exit
}
class=(arabidopsis budding fission mammalian tcrNet thelper)
SUF=""
RUN="LFDT.pyc"
Write=0
NoR=""
NoC=""
NoG=""
NoQ=""
## proces the options
LPS="budding"
while getopts "ncgqfl:" arg
do
  case $arg in
   n) NoR="-n";;
   c) NoC="-c";;
   g) NoG="-g";;
   q) NoQ="-q";;
   l) LPS=$OPTARG
      YES="no"
      for cn in ${class[*]}; do
        if [ "$cn" != "$LPS" ]; then
          continue
        else
          YES="yes"; break
        fi
      done 
      if [ "$YES" == "no" ]; then
        usage
      fi;;
   f) Write=1;;
   ?) echo "unkonwn options"; usage;;
  esac
done 

N=10
SUF="$NoR$NoC$NoG"
if [ $Write == 1 ]; then
  Home="llp"$NoR$NoC$NoG
  if [ -d $Home/$LPS ]; then
    rm -fr $Home/$LPS
  fi
  mkdir $Home/$LPS
fi

if [ -f $LPS$SUF.res ]; then
  rm -f $LPS$SUF.res
fi

INS="10 20 40 80 160 320 640"
for I in $INS
do
  J=2
  while((J<=10))
  do
     K=1
     while ((K<=N))
     do
       echo "--------------" >> $LPS$SUF.res
       echo $LPS-$I-$J-$K >> $LPS$SUF.res
       echo `date` >> $LPS$SUF.res
       if [ $Write == 1 ]; then
         python3.6 $RUN -t 1800 $NoR $NoG $NoC $NoQ -f \
		$Home/$LPS/$I-$J-$K.lp data/$LPS/$I-$J-$K 2>&1 >> $LPS$SUF.res
       else
         python3.6 $RUN -t 1800 $NoR $NoG $NoC $NoQ \
		data/$LPS/$I-$J-$K 2>&1 >> $LPS$SUF.res
       fi
       let K=K+1
     done
     let J=J+2 
  done
done
