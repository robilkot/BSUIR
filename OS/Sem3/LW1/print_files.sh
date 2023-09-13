#!/bin/bash

# example: ./print_files.sh output2.txt ../../.. md

output_file=output.txt
dir=.

if [ $1 ]; then 
	output_file=$1
fi

if [ $2 ]; then
	dir=$2
fi


if [ $3 ]; 
then
	for file in `find $dir -maxdepth 1 -type f -name "*$3"`
	do
		echo $file;
	done > $output_file
else
	for file in `find $dir -maxdepth 1 -type f ! -name "*.*"`
	do
		echo $file;
	done > $output_file
fi
