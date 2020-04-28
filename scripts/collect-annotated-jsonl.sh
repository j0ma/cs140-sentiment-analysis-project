#!/bin/sh

CURRENTLY_IN_SCRIPTS_FOLDER=$(pwd | grep -o "/scripts$")
OUTPUT_FOLDER="./data/annotated"

mkdir -p $OUTPUT_FOLDER

if [ ! -z $CURRENTLY_IN_SCRIPTS_FOLDER ]
then
    echo "Currently in ./scripts, moving to root ..."
    cd .. # we want to be in the repo root folder
fi

FILES="warren-annotated-zhuoran-huang.jsonl Server/biden-annotated-yonglin-wang.jsonl  Server/buttigieg-annotated-xiaoyu-lu.jsonl"

for f in $FILES
do
    bare_fname=$(echo $f | sed s/"Server\/"/""/g)
    out_path="${OUTPUT_FOLDER}/${bare_fname}"
    echo "moving: ${f} -> ${out_path}"
    mv $f $out_path
done

echo "Done! Here is ${OUTPUT_FOLDER}"
ls $OUTPUT_FOLDER
