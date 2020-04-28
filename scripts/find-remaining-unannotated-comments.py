# find-remaining-unannotated-comments.py

# Description: Takes the annotated comments as well as the 500
#              assigned ones and sees which comments in the 500
#              are still unannotated

# 500 comments come from
# ../data/comments_for_annotators
# └── 500
    # ├── biden.500.jsonl
    # ├── buttigieg.500.jsonl
    # ├── sanders.500.jsonl
    # ├── warren.500.jsonl
    # └── yang.500.jsonl

import json
import sys
import os

# check if we are in ./scripts/ as we should be
WORKING_DIR = os.getcwd()
if not WORKING_DIR.endswith('/scripts'):
    sys.exit('Must run script while in <repo_root>/scripts folder!')

CANDIDATES = ['biden', 'buttigieg', 'sanders', 'warren', 'yang']

DATA_PATH=os.path.abspath("../data/")
ANNOTATION_FOLDER_PATH=f"{DATA_PATH}/annotated"

ALREADY_ANNOTATED_FILES = {
    "biden": "biden-annotated-yonglin-wang.jsonl",
    "buttigieg": "buttigieg-annotated-xiaoyu-lu.jsonl",
    "warren": "warren-annotated-zhuoran-huang.jsonl"
}

ASSIGNED_500 = f"{DATA_PATH}/comments-for-annotators/500"
ASSIGNED_FILES = {
    cand: f"{cand}.500.jsonl"
    for cand in CANDIDATES
}

if __name__ == '__main__':
   
    try:
        candidate = sys.argv[1]
    except IndexError:
        sys.exit('Need to supply candidate as 1st command line arg!')

    if candidate not in ALREADY_ANNOTATED_FILES:
        #print(f'{candidate} has not been annotated yet!')
        sys.exit(0)
    
    annotated_file = ALREADY_ANNOTATED_FILES[candidate]
    annotated_path = f"{DATA_PATH}/annotated/{annotated_file}"
    assigned_file = ASSIGNED_FILES[candidate]
    assigned_path = f"{DATA_PATH}/comments_for_annotators/500/{assigned_file}"

    with open(annotated_path, 'r') as f:
        annotated_lines = [json.loads(l) for l in f]
        annotated_elems = {(candidate, d['comment']) for d in annotated_lines}

    for l in open(assigned_path, 'r'):
        d = json.loads(l)
        comment = d['comment']
        if (candidate, comment) not in annotated_elems:
            sys.stdout.write(l)
