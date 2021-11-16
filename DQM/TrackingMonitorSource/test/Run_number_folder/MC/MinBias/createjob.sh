#!/bin/bash
mkdir -p step1_output log
workdir=$(echo $PWD)
echo $workdir
i=1
while [ $i -lt 214 ]
  do
    j=$(($i+0))
    fnames=$(echo $(sed -n "$i,$j p" filelist.txt))
    echo $i,$j
    echo $fnames
    sed -e "s@PWD@$workdir@g" \
	-e "s@INPUTFILES@$fnames@g" \
        -e "s@INDEX@$i@g" step1_cfg.py.tmpl > "step1_"$i"_cfg.py"
    sed -e "s@PWD@$workdir@g" \
	-e "s@INDEX@$i@g" submit.sh.tmpl > "submit_"$i".sh"
    sed -e "s@PWD@$workdir@g" \
        -e "s@INDEX@$i@g" batch.sub.tmpl > "batch_"$i".sub"
    chmod 755 "submit_"$i".sh"
    condor_submit "batch_"$i".sub"
    i=$(($i+1))
done
