import itertools as it
import pandas as pd
import json
import os

OUTPUT_FOLDER = "./data/final-corpus.csv"
PREFIX = "./data/annotated"

def load_json(p):
    with open(p, 'r') as f:
        return [json.loads(l) for l in f]

def get_name(filename):
    hyphen_ix = filename.index('-')
    name = filename[:hyphen_ix]
    return name

def process_comment(c):
    output = []
    comment = c['comment']
    aspects = c['aspects']
    targets = [a.replace('target_', '') for a in aspects]
    aspects_per_candidate = [(t, aspects['target_{}'.format(t)]) for t in targets]
    for t, apc in aspects_per_candidate:
        out = {}
        out['target'] = t
        out['comment'] = comment
        for a in apc:
            values = a.split("_")
            polarity = values.pop()
            aspect = "_".join(values)
            out[aspect] = polarity
        output.append(out)
    return output

def flatten(nested):
    return list(it.chain.from_iterable(nested))

if __name__ == '__main__':
    print("Loading filenames...")
    filenames = os.listdir(PREFIX)
    all_annotations = {}
    for fn in filenames:
        n = get_name(fn)
        all_annotations[n] = load_json("{}/{}".format(PREFIX, fn))

    # merge everything into one
    print('Merging annotations...')
    processed_annotations = flatten([flatten([process_comment(c) for c in all_annotations[cand]]) for cand in all_annotations])
    output = pd.DataFrame(processed_annotations)
    comment_ids = {c: ix for ix, c in enumerate(output.comment.unique())}
    output['comment_id'] = output.comment.apply(lambda c: comment_ids[c])
    print(f'Done! Saving to: {OUTPUT_FOLDER}')
    output.to_csv(OUTPUT_FOLDER, index=False, encoding='latin1')
