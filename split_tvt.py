import nltk
import sklearn
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification



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