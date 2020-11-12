#!/bin/bash
echo "GCP Storage Meta Data Utility version 1.2" 
if [ "$1" == "" ]; 
then 
	echo "Missing Bucket Name" 
	exit
else 
	gsutil ls -L -b  gs://$1
fi
