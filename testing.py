import array
import numpy as np

arrays = []
for line in open("rt-polarity.pos.txt"):

    new_array = np.array((array.float(i) for i in line.split(' ')))
    arrays.append(new_array)

    # negative vocab
    counterneg = Counter(neg)
    for word, count in counterneg.items():
        negCount = ("{}:{}".format(word, count))

''' 
index = 1
word_to_index = {}
for word in pos.split():
    if word in word_to_index:
        # already seen
        continue
    word_to_index[word.lower()] = index
    index += 1


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

'''