import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import classification_report

INPUT_PATH = "../data/final-corpus.csv"
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


def is_policy_race(row):
    pr = row['policy_race']
    return bool(pr == 'positive')


def is_appeal_white(row):
    aw = row['appeal_white']
    return bool (aw == 'positive')


def is_policy_unspecified(row):
    pu = row['policy_unspecified']
    return bool (pu == 'positive')


def is_policy_other(row):
    po = row['policy_other']
    return bool (po == 'positive')


def is_policy_international(row):
    pi = row['policy_international']
    return bool (pi == 'positive')


def is_policy_healthcare(row):
    ph = row['policy_healthcare']
    return bool(ph == 'positive')


def is_policy_economy(row):
    pe = row['policy_economy']
    return bool(pe == 'positive')


def is_policy_education(row):
    pe = row['policy_education']
    return bool (pe == 'positive')


def is_policy_lgbt(row):
    pl = row['policy_lgbt']
    return bool (pl == 'positive')


def is_appeal_old(row):
    ao = row['appeal_old']
    return bool (ao == 'positive')


def is_appeal_african(row):
    aa = row['appeal_african']
    return bool (aa == 'positive')


def is_appeal_democrat(row):
    ad = row['appeal_democrat']
    return bool (ad == 'positive')


def is_appeal_other(row):
    ao = row['appeal_other']
    return bool (ao == 'positive')


def is_appeal_young(row):
    ay = row['appeal_young']
    return bool (ay == 'positive')


def is_appeal_unspecified(row):
    au = row['appeal_unspecified']
    return bool (au == 'positive')


def is_appeal_female(row):
    af = row['appeal_female']
    return bool (af == 'positive')


def is_appeal_asian(row):
    aa = row['appeal_asian']
    return bool (aa == 'positive')


def is_appeal_hispanic(row):
    ah = row['appeal_hispanic']
    return bool (ah == 'positive')


# create features
Y_target = target
Y_policy = corpus.apply(lambda r: is_policy_comment(r, cols), axis=1)
Y_appeal = corpus.apply(lambda r: is_appeal_comment(r, cols), axis=1)
Y_cp = corpus.apply(lambda r: is_campaign_prospects_comment(r), axis=1)
Y_positive = corpus.apply(lambda r: is_generally_positive(r), axis=1)
Y_policy_race = corpus.apply(lambda r: is_generally_positive(r), axis=1)
Y_appeal_white = corpus.apply(lambda r: is_generally_positive(r), axis=1)
Y_policy_unspecified = corpus.apply(lambda r: is_generally_positive(r), axis=1)
Y_policy_other = corpus.apply(lambda r: is_generally_positive(r), axis=1)
Y_policy_international = corpus.apply(lambda r: is_generally_positive(r), axis=1)
Y_policy_healthcare = corpus.apply(lambda r: is_policy_healthcare(r), axis=1)
Y_policy_economy = corpus.apply(lambda r: is_policy_economy(r), axis=1)
Y_policy_education = corpus.apply(lambda r: is_policy_education(r), axis=1)
Y_policy_lgbt = corpus.apply(lambda r: is_policy_lgbt(r), axis=1)
Y_appeal_old = corpus.apply(lambda r: is_appeal_old(r), axis=1)
Y_appeal_african = corpus.apply(lambda r: is_appeal_african(r), axis=1)
Y_appeal_democrat = corpus.apply(lambda r: is_appeal_democrat(r), axis=1)
Y_appeal_other = corpus.apply(lambda r: is_appeal_other(r), axis=1)
Y_appeal_young = corpus.apply(lambda r: is_appeal_young(r), axis=1)
Y_appeal_unspecified = corpus.apply(lambda r: is_appeal_unspecified(r), axis=1)
Y_appeal_female = corpus.apply(lambda r: is_appeal_female(r), axis=1)
Y_appeal_asian = corpus.apply(lambda r: is_appeal_asian(r), axis=1)
Y_appeal_hispanic = corpus.apply(lambda r: is_appeal_hispanic(r), axis=1)

# target,comment,general,policy_race,appeal_white,policy_unspecified,policy_other,policy_international,policy_healthcare,policy_economy,campaign_prospects,policy_education,policy_lgbt,appeal_old,appeal_african,appeal_democrat,appeal_other,appeal_young,appeal_unspecified,appeal_female,appeal_asian,appeal_hispanic,

labels = [Y_target, Y_policy, Y_appeal, Y_cp, Y_positive, Y_policy_race, Y_appeal_white,Y_policy_unspecified,
          Y_policy_other,Y_policy_international, Y_policy_healthcare,Y_policy_economy,Y_policy_education,
          Y_policy_lgbt, Y_appeal_old, Y_appeal_african, Y_appeal_democrat, Y_appeal_other, Y_appeal_young,
          Y_appeal_unspecified, Y_appeal_female, Y_appeal_asian, Y_appeal_hispanic]

## labels = [Y_target, Y_policy, Y_appeal, Y_cp, Y_positive]
short_names = ['target', 'policy','voter_appeal', 'campaign_prospects', 'general','policy_race','appeal_white','policy_unspecified',
               'policy_other','policy_international','policy_healthcare','policy_economy','policy_education',
               'policy_lgbt', 'appeal_old', 'appeal_african', 'appeal_democrat', 'appeal_other', 'appeal_young',
               'appeal_unspecified', 'appeal_female', 'appeal_asian', 'appeal_hispanic']
names = ['Who is the target?', 
         'Is the comment about policy?', 
         'Is the comment about voter appeal?', 
         'Is the comment about campaign prospects?', 
         'Is the comment generally positive?',
         'Is the comment about race under policy positive?',
         'Is the comment about white under appeal positive?',
         'Is the comment unspecified under policy positive?',
         'Is the comment about other under policy positive?',
         'Is the comment about international under policy positive?',
         'Is the comment about health care under policy positive?',
         'Is the comment about economy under policy positive?',
         'Is the comment about education under policy positive?',
         'Is the comment about lgbt under policy positive?',
         'Is the comment about old under appeal positive?',
         'Is the comment about african under appeal positive?',
         'Is the comment about democrat under appeal positive?',
         'Is the comment about other under appeal positive?',
         'Is the comment about young under appeal positive?',
         'Is the comment unspecified under appeal positive?',
         'Is the comment about female under appeal positive?',
         'Is the comment about asian under appeal positive?',
         'Is the comment about hispanic under appeal positive?']
cv = CountVectorizer()
tf = TfidfVectorizer()

X_cv = cv.fit_transform(comment)
X_tf = tf.fit_transform(comment)

# logistic regressions
logregs_cv = [LogisticRegression(max_iter=1000) for y in labels]
logregs_tf = [LogisticRegression(max_iter=1000) for y in labels]

res = {'cv': {}, 'tf': {}}

print('Predicting using regular BoW features:')
for sn, name, y, lr in zip(short_names, names, labels, logregs_cv):
    lr.fit(X=X_cv, y=y)
    y_pred = lr.predict(X_cv)
    res['cv'][f'{sn}_true'] = y
    res['cv'][sn] = y_pred
    report = classification_report(y_pred=y_pred, y_true=y)
    print(name)
    print(report)

print('Predicting using TF-IDF features:')
for sn, name, y, lr in zip(short_names, names, labels, logregs_tf):
    lr.fit(X=X_tf, y=y)
    res['tf'][f'{sn}_true'] = y
    res['tf'][sn] = y_pred
    y_pred = lr.predict(X_tf)
    report = classification_report(y_pred=y_pred, y_true=y)
    print(name)
    print(report)

print('Prediction using also candidate names.')
print('Here both the target and aspect must be right!')
print("First using BOW features:")

cv_res = res['cv']
for sn, name in zip(short_names, names):
    pred = [f"{t}_{sn}" for t, sn in zip(cv_res['target'], cv_res[sn])]
    truth = [f"{t}_{sn}" for t, sn in zip(cv_res['target_true'], cv_res[f'{sn}_true'])]
    report = classification_report(y_pred=pred, y_true=truth)
    print(name)
    print(report)

    
