#!/bin/sh

INPUT_FOLDER='../data'
OUTPUT_FOLDER=${INPUT_FOLDER}/comments_for_annotators
SAMPLES_PER_CANDIDATE=200
SEED_FILE='../README.md'

echo "Welcome to the comment sampling script!"

echo "Creating output folder..."
mkdir -p $OUTPUT_FOLDER

for INPUT_FILE in ${INPUT_FOLDER}/*.jsonl;
do
    CAND=$(echo $INPUT_FILE | grep -Eo "\w+.jsonl$" | sed s/\.jsonl//g)
    echo "Sampling ${SAMPLES_PER_CANDIDATE} rows from ${CAND}"
    OUTPUT_FILE=$(
        echo $INPUT_FILE | \
            sed "s/\.jsonl/\.200.jsonl/g" | \
            sed "s/\.\.\/data/\.\.\/data\/comments_for_annotators/g"
    )
    shuf \
        --random-source=${SEED_FILE} \
        --head-count ${SAMPLES_PER_CANDIDATE} \
        ${INPUT_FILE} > ${OUTPUT_FILE}
done

