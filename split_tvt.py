import nltk
import random
from collections import Counter, defaultdict
import numpy as np

with open("rt-polarity.pos.txt", 'r') as f:
    pos = f.read().split(' ')

with open("rt-polarity.neg.txt", 'r') as f:
    neg = f.read().split(' ')

''' 
index = 1
word_to_index = {}
for word in pos.split():
    if word in word_to_index:
        # already seen
        continue
    word_to_index[word.lower()] = index
    index += 1
'''

# positive vocab
counterpos = Counter(pos)
for word, count in counterpos.items():
    posCount = ("{}:{}".format(word, count))

# pos count
mypos = {}
i = 0
for item in pos:
    if (i > 0 and item in mypos):
        continue
    else:
        i = i + 1
        mypos[item] = i

p = []
for item in pos:
    p.append(mypos[item])

posVec = np.array(p, dtype=int)

print(posVec)

# negative vocab
counterneg = Counter(neg)
for word, count in counterneg.items():
    negCount = ("{}:{}".format(word, count))

# neg count
myneg = {}
i = 0
for item in neg:
    if (i > 0 and item in myneg):
        continue
    else:
        i = i + 1
        myneg[item] = i

n = []
for item in neg:
    n.append(myneg[item])

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
