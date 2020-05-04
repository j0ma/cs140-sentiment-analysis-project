import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import classification_report

INPUT_PATH = "./data/final-corpus.csv"
corpus = pd.read_csv(INPUT_PATH).fillna(0)
comment = corpus.comment
target = corpus.target
cols = corpus.columns

def is_policy_comment(row, cols):
    policy_cols = [c for c in cols if c.startswith('policy')]
    out = any([row[pc] for pc in policy_cols])
    return out

def is_appeal_comment(row, cols):
    policy_cols = [c for c in cols if c.startswith('appeal')]
    out = any([row[pc] for pc in policy_cols])
    return out

def is_campaign_prospects_comment(row):
    cp = row.campaign_prospects#.tolist().pop()
    return bool(cp)

def is_generally_positive(row):
    g = row['general']#.tolist().pop()
    return bool(g == 'positive')

# create features
Y_target = target
Y_policy = corpus.apply(lambda r: is_policy_comment(r, cols), axis=1)
Y_appeal = corpus.apply(lambda r: is_appeal_comment(r, cols), axis=1)
Y_cp = corpus.apply(lambda r: is_campaign_prospects_comment(r), axis=1)
Y_positive = corpus.apply(lambda r: is_generally_positive(r), axis=1)
labels = [Y_target, Y_policy, Y_appeal, Y_cp, Y_positive]
names = ['Who is the target?', 
         'Is the comment about policy?', 
         'Is the comment about voter appeal?', 
         'Is the comment about campaign prospects?', 
         'Is the comment generally positive?']
cv = CountVectorizer()
tf = TfidfVectorizer()

X_cv = cv.fit_transform(comment)
X_tf = tf.fit_transform(comment)

# logistic regressions
logregs_cv = [LogisticRegression(max_iter=1000) for y in labels]
logregs_tf = [LogisticRegression(max_iter=1000) for y in labels]

print('Predicting using regular BoW features:')
for name, y, lr in zip(names, labels, logregs_cv):
    lr.fit(X=X_cv, y=y)
    y_pred = lr.predict(X_cv)
    report = classification_report(y_pred=y_pred, y_true=y)
    print(name)
    print(report)

print('Predicting using TF-IDF features:')
for name, y, lr in zip(names, labels, logregs_tf):
    lr.fit(X=X_tf, y=y)
    y_pred = lr.predict(X_tf)
    report = classification_report(y_pred=y_pred, y_true=y)
    print(name)
    print(report)
