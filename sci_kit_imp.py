from collections import Counter, defaultdict

from sklearn.feature_extraction.text import TfidfVectorizer

with open("rt-polarity.pos.txt", 'r') as f:
    test_data = f.read().split(' ')

with open("rt-polarity.neg.txt", 'r') as f:
    test_data = f.read().split(' ')


