import json
import pandas as pd


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

with open('./data/all_comments.json', 'r') as f:
    comments_dataset = json.loads(f.read())

all_comments_df = load_comments('all')

def make_rows_readable(df):
    out = []
    for ix, row in df.iterrows():
        pretty = []
        for c in row.index:
            pretty.append(f"{c}: {row[c]}")
        pretty = "\n".join(pretty)
        out.append(pretty)
    return "\n#####\n".join(out)

def search_for_comment(s, k=1):
    """
    Finds the top k results containing s in the comment string.
    """

    subset = all_comments_df[all_comments_df.comment.str.contains(s)].head(k)
    output = make_rows_readable(subset)
    return output
