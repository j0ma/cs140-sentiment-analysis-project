import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import classification_report

INPUT_PATH = "../data/final-corpus.csv"
corpus = pd.read_csv(INPUT_PATH)
comment = corpus.comment
target = corpus.target

# create features
cv = CountVectorizer()
tf = TfidfVectorizer()

X_cv = cv.fit_transform(comment)
X_tf = tf.fit_transform(comment)
y = target

# logistic regression
lr_cv = LogisticRegression(max_iter=1000)
lr_tf = LogisticRegression(max_iter=1000)
lr_cv.fit(X=X_cv, y=y)
lr_tf.fit(X=X_tf, y=y)

# get predictions
y_pred_cv = lr_cv.predict(X_cv)
y_pred_tf = lr_tf.predict(X_tf)

# compute classification report
report_cv = classification_report(y_true=y, y_pred=y_pred_cv)
report_tf = classification_report(y_true=y, y_pred=y_pred_tf)

print('Report for CountVectorizer')
print(report_cv)

print('Report for TFIDFVectorizer')
print(report_tf)
