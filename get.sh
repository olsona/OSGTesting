#!/bin/bash

unset HTTP_PROXY

while getopts f:m:p:r: opt 
do
    case "${opt}"
    in
	f) FILE=${OPTARG};;
	m) METHOD=${OPTARG};;
	p) FPATH=${OPTARG};;
	r) RESOURCE=${OPTARG};;
    esac
done
echo $RESOURCE
echo $METHOD
if [ "${METHOD}" = wget ]; then
    start=$(date '+%s%3N')
    wget --no-check-certificate ${FPATH}/${FILE}
    end=$(date '+%s%3N')
    if [ -s $FILE ]; then
	echo $((end-start))
	rm $FILE
    else
	echo "Wget unsuccessful"
    fi
elif [ "${METHOD}" = curl ]; then
    start=$(date '+%s%3N')
    curl -L -O ${FPATH}/${FILE}
    end=$(date '+%s%3N')
    if [ -s $FILE ]; then
	echo $((end-start))
	rm $FILE
    else
	echo "Curl unsuccessful"
    fi
elif [ "${METHOD}" = urllib ]; then
    python get.py -f $FILE -p $FPATH
fi