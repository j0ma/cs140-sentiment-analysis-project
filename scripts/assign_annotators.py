import random
from collections import defaultdict

SEED=12345
random.seed(SEED)

ANNOTATORS = [
  "Yonglin Wang",
  "Zhuoran Huang",
  "Shiyi Shen",
  "Xiaoyu Lu"
]

CANDIDATES = [
  "Joe Biden",
  "Bernie Sanders",
  "Andrew Yang",
  "Elizabeth Warren",
  "Pete Buttigieg"
]

ASSIGNMENTS = defaultdict(list)
if __name__ == '__main__':
    random.shuffle(ANNOTATORS)
    random.shuffle(CANDIDATES)
    for ann, cand in zip(ANNOTATORS, CANDIDATES):
        ASSIGNMENTS[ann].append(cand)
    remaining_candidate = CANDIDATES[-1]
    random_annotator = random.choice(ANNOTATORS)
    ASSIGNMENTS[random_annotator].append(remaining_candidate)

    shiyi_cand = ASSIGNMENTS['Shiyi Shen']
    for c in shiyi_cand:
        rand_ann = random.choice(ANNOTATORS)
        while rand_ann == 'Shiyi Shen':
            rand_ann = random.choice(ANNOTATORS)
        ASSIGNMENTS[rand_ann].append(c)
    
    del ASSIGNMENTS['Shiyi Shen']

    for ann, cands in ASSIGNMENTS.items():
        print(f"{ann}: {', '.join(cands)}")

    
