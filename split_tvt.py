import nltk
import random
from collections import Counter, defaultdict
import numpy as np
import re

with open("rt-polarity.pos.txt", 'r') as f:
    pos = f.read().replace('\n', '')

with open("rt-polarity.neg.txt", 'r') as f:
    neg = f.read().replace('\n', '')

posSentences = []
while pos.find('.') != -1:
    index = pos.find('.')
    posSentences.append(pos[:index + 1])
    pos = pos[index + 1:]

negSentences = []
while neg.find('.') != -1:
    index = neg.find('.')
    negSentences.append(neg[:index + 1])
    neg = neg[index + 1:]

pos_matrix = []
for pos_sentence in posSentences:
    pos_matrix.append(pos_sentence.strip().split(' '))

neg_matrix = []
for neg_sentence in negSentences:
    neg_matrix.append(neg_sentence.strip().split(' '))

    # positive vocab
    posC = Counter()
    for xs in pos_matrix:
        for x in set(xs):
            posC[x] += 1

            print(posC)



'''
i = iter(pos_matrix)
posVec = dict(zip(i, i))

i = iter(neg_matrix)
negVec = dict(zip(i, i))

print(posVec)
'''

'''Split Data
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


convert
text
into
vectors
c = 0.10, c = 0.100: one
of
these
will
be
the
most
accurate! find
through
validation
set:
for hw
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
from sklearn.svm import SVC

clf = SVC()
clf.fit(X, y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

print(clf.predict([[-0.8, -1]]))
'''
