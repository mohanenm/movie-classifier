import math
import re
from collections import OrderedDict
from itertools import islice
import collections

positive = open("rt-polarity.pos.txt", "r")
negative = open("rt-polarity.neg.txt", "r")
validation = open("develop.txt", "w")
vector = open("Vectors.txt", "w")
test_file = open("test_vec.txt", "w")

posRev = [
    line.strip() for line in positive
]
negRev = [
    line.strip() for line in negative
]

trainneg = math.floor(.7 * len(negRev)) - 1
val_neg = math.floor(.15 * len(negRev)) - 1
testneg = math.floor(.15 * len(negRev)) - 1

trainpos = math.floor(.7 * len(posRev)) - 1
val_pos = math.floor(.15 * len(posRev)) - 1
testpos = math.floor(.15 * len(posRev)) - 1

neg_train = negRev[0:trainneg]
neg_dev = negRev[trainneg + 1:trainneg + 1 + val_neg]
neg_test = negRev[trainneg + val_pos + 1:trainpos + val_pos + 1 + testneg]
pos_train = posRev[0:trainpos]
pos_dev = posRev[trainpos + 1:trainpos + 1 + val_pos]
pos_test = posRev[trainpos + val_pos + 1:trainpos + val_pos + 1 + testpos]

posdict = dict()
for i in range(len(pos_train)):
    l_s = re.sub(r'[^\w\s]', '', pos_train[i]).lower().split()
    for j in l_s:
        posdict[j] = posdict.get(j, len(posdict))
negdict = dict()
for i in range(len(neg_train)):
    l_s = re.sub(r'[^\w\s]', '', neg_train[i]).lower().split()
    for j in l_s:
        negdict[j] = negdict.get(j, len(negdict))

mergedDict = {**posdict, **negdict}



 for i in range(len(negdict)):
    validation.write("-1 ")
    vector.write("-1 ")
    test_file.write("-1 ")
    currentline = dict()
    a = re.sub(r'[^\w\s]', '', neg[i]).lower().split()
    for j in a:
        if j in neg:
            currentline[final[j]] = currentline.get(final[j], 0) + 1
    finalDict = collections.OrderedDict(sorted(currentline.items()))
    for key, value in finalDict.items():
        validation.write("%d:%d " % (key, value))
        vector.write("%d:%d " % (key, value))
        test_file.write("%d:%d " % (key, value))
    validation.write("\n")
    vector.write("\n")
    test_file.write("\n")

 for i in range(len(posdict)):
    validation.write("+1 ")
    vector.write("+1 ")
    test_file.write("+1 ")
    currentline = dict()
    a = re.sub(r'[^\w\s]', '', pos[i]).lower().split()
    for j in a:
        if j in pos:
            currentline[final[j]] = currentline.get(final[j], 0) + 1
    finalDict = collections.OrderedDict(sorted(currentline.items()))
    for key, value in finalDict.items():
        validation.write("%d:%d " % (key, value))
        vector.write("%d:%d " % (key, value))
        test_file.write("%d:%d " % (key, value))
    validation.write("\n")
    vector.write("\n")
    test_file.write("\n")




    for i in range(len(pos)):
        line = dict()
        a = re.sub(r'[^\w\s]', '', pos[i]).lower().split()
        for j in a:
            if j in dic:
                currentline[dic[j]] = currentline.get(dic[j], 0) + 1
        od = collections.OrderedDict(sorted(currentline.items()))
        for key, value in od.items():
            ("%d:%d " % (key, value))
        file.write("\n")



'''
i = iter(pos_matrix)
posVec = dict(zip(i, i))

i = iter(neg_matrix)
negVec = dict(zip(i, i))

print(posVec)

Split Data
train = pos[:int((.7) * len(pos))] + neg[:int((.7) * len(neg))]
test = pos[int((.85) * len(pos)):] + neg[int((.85) * len(neg)):]
validate = pos[int((.85) * len(pos)):] + neg[int((.85) * len(neg)):]

print(len(train))  # 70%
print(len(test))  # 15%
print(len(validate))  # 15%
'''

'''
df = pd.DataFrame({'text': [[pos],
                            [neg]]})

L = [train]


def f(x): Counter([y for y in x if y in L])


df['new'] = (pd.DataFrame(df['text'].apply(f).values.tolist()).fillna(0).astype(int).reindex(columns=L).values.tolist())
print(df)



classifier = LinearSVC(c=0.1)
< list
of
vectors >, < list
of
labels >
classifier.fit(x_train, y_train)
classifier.predict( < training
examples >)

import numpy as np


X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
'''

from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification

clf = SVC("test_vec.txt", "test_vec.txt")
clf.fit(X, y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

print(clf.predict([[-0.8, -1]]))

