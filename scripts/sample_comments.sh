#!/bin/sh

INPUT_FOLDER='../data'

SAMPLES_PER_CANDIDATE=$1

if [ -z $SAMPLES_PER_CANDIDATE ]
then
    SAMPLES_PER_CANDIDATE=200
fi

OUTPUT_FOLDER=${INPUT_FOLDER}/comments_for_annotators/${SAMPLES_PER_CANDIDATE}
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
            sed "s/\.jsonl/\.${SAMPLES_PER_CANDIDATE}.jsonl/g" | \
            sed "s/\.\.\/data/\.\.\/data\/comments_for_annotators\/${SAMPLES_PER_CANDIDATE}/g"
    )
    shuf \
        --random-source=${SEED_FILE} \
        --head-count ${SAMPLES_PER_CANDIDATE} \
        ${INPUT_FILE} > ${OUTPUT_FILE}
done

