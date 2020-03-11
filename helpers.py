import json

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

def format_comment(triplet):
    comment, date, author = triplet
    return f"Author: {author}\nDate: {date}\nComment: {comment}"


