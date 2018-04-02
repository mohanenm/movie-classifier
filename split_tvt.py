import random
from collections import Counter
from operator import mul
from nltk import word_tokenize
import numpy as np
import pandas as pd

pos = []
with open("rt-polarity.pos.txt") as p:
    for words in p:
        pos.append(words), 'pos'

neg = []
with open("rt-polarity.neg.txt") as p:
    for words in p:
        neg.append(words), 'neg'
print(len(pos))
print(len(neg))

'''Split Data'''
train = pos[:int((.7) * len(pos))] + neg[:int((.7) * len(neg))]
test = pos[int((.85) * len(pos)):] + neg[int((.85) * len(neg)):]
validate = pos[int((.85) * len(pos)):] + neg[int((.85) * len(neg)):]

print(len(train))  # 70%
print(len(test))  # 15%
print(len(validate))  # 15%


df = pd.DataFrame({'text': [[pos],
                            [neg]]})

L = [train]


def f(x): Counter([y for y in x if y in L])


df['new'] = (pd.DataFrame(df['text'].apply(f).values.tolist()).fillna(0).astype(int).reindex(columns=L).values.tolist())
print(df)

'''
pos = open("rt-polarity.pos.txt", 'r').read()
tokens = word_tokenize(pos)
tokens_final = [item.lower() for item in tokens]
i_counter = Counter(tokens_final)
t_count = len(tokens_final)

for word in i_counter:
    i_counter[word] /= float(t_count)
    print(sum(i_counter.values()))

    from functools import reduce
text_rand = []
for _ in range(100):
    r = random.random()
    counter_rand = .0

    for word, freq in (i_counter.items()):
        counter_rand += freq

        if counter_rand > r:
            text_rand.append(word)
            break

print(' '.join(text_rand))

print(reduce(mul, [i_counter[a] for a in text_rand], 1.0))



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
