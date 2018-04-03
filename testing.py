import array
import numpy as np

arrays = []
for line in open("rt-polarity.pos.txt"):

    new_array = np.array((array.float(i) for i in line.split(' ')))
    arrays.append(new_array)

