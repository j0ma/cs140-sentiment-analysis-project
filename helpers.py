import json
import pandas as pd

with open('./data/all_comments.json', 'r') as f:
    comments_dataset = json.loads(f.read())

def triplets(arr):
    """
    Yields elements of `arr` as 3-tuples:
    (a_t, a_(t+1), a_(t+2)) for t = 0, 1, ..., len(arr)-3
    """
    N = len(arr)
    i = 0
    while i < N-1:
        yield arr[i:i+3]
        i += 3

def load_comments(candidate_name=None):
    if not candidate_name or candidate_name=='all':
        return pd.read_csv('data/all_comments.csv', lineterminator='\n')
    else:
        return pd.read_csv(f'data/{candidate_name}.csv', lineterminator='\n')

