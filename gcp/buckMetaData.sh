#!/bin/bash
echo "Bucket Meta Data Utility" 
if [ "$1" == "" ]; 
then 
	echo "Missing Bucket Name" 
	exit
else 
	gsutil ls -L -b  gs://$1
fi
