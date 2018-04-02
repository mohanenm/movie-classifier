import nltk
import sklearn
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification

pos = []
with open("rt-polarity.pos.txt") as p:
    for words in p:
        pos.append([format_sentence(words), 'pos'])

neg = []
with open("rt-polarity.neg.txt") as p:
    for words in p:
        neg.append([format_sentence(words), 'neg'])

        data = open("westPhil.txt", 'r').read()
        tokens = word_tokenize(data)
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

'''
training = pos[int((.8) * len(pos))] + neg[:int((.8) * len(neg))]
test = pos[int((.8) * len(pos)):] + neg[int((.8) * len(neg))]
validation = pos[int((.8) * len(pos)):] + neg[int((.8) * len(neg))]
'''

''' convert text into vectors'''
''' c = 0.10, c = 0.100: one of these will be the most accurate! find through validation set: for hw'''
classifier = LinearSVC(c = 0.1)
''' <list of vectors>, <list of labels>'''
classifier.fit(x_train, y_train)
classifier.predict(<training examples>)

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