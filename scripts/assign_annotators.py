import random
from collections import defaultdict

SEED=12345
random.seed(SEED)

ANNOTATORS = [
  "Yonglin Wang",
  "Zhuoran Huang",
  "Shiyi Shen",
  "Xiaoyu Lu",
  "Linxuan Yang"
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
    for ann, cands in ASSIGNMENTS.items():
        print(f"{ann}: {', '.join(cands)}")


