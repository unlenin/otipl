#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from sklearn import linear_model
from sklearn.ensemble import ExtraTreesClassifier

def load_data(data_file):
    table = [ l.split() for l in open(data_file).readlines() ] # features + classes
    features = len(table[0])
    data = np.empty(shape=(len(table), features))

    for (i, l) in enumerate(table):
        data[i] = table[i]
    
    return data

train = load_data("training.txt")

test = load_data("test.txt")

result = open("result.txt", "w") # features + classes + predicted classes

X = train[:, :-1]
Y = train[:, -1]

clf = ExtraTreesClassifier(compute_importances=True, random_state=0)
X_new = clf.fit(X, Y).transform(X)

thres = sorted(clf.feature_importances_, reverse=True)[X_new.shape[1] - 1]
selected = [ i for (i, f) in enumerate(clf.feature_importances_) if f >= thres ]

logreg = linear_model.LogisticRegression(C=1e5)

logreg.fit(X_new, Y)

X_test = test[:, selected]

Z = logreg.predict(X_test)

res = np.append(test, Z[..., None], 1)

for r in res:
    result.write("\t".join(map(str, r)) + "\n")

