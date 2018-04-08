import re

pos_adjective = open("pos_words").read()
neg_adjective = open("neg_words").read()

pos = pos_adjective.split()
neg = neg_adjective.split()

'''
this should positive
'''
# print("this should be pos:")

data = open("rt-polarity.pos.txt").read()

'''

check the list of positive words against 
the movie review(whatever that may be
***define a function that take a file as 
input and crosschecks the words on the 
positive word list with the movie review
and if they are more than ten matches.....
if there are more than ten words...return 
postive, if the number of words in each 
match, return 'neutral' if there are more 
negative words, then print that the review
is negative. 

How can I check the list of negative words?

I can instead, print out, "most likely 
positive or most likely negative. 

compare these results with with the bayes 
training deviceeeeeee


'''

'''

if any(i in pos for i in ):

elif any(i in neg for i in data):

if posCount > negCount:
    print("This review is most likely positive")

elif negCount > posCount:
    print("This review is most likely positive")

elif posCount == negCount:
    print("equal")
else:
    print("Default")

'''
'''
this should return negative
'''
'''
print("this should be neg:")
data2 = open("rt-polarity.pos.txt").read()
if any(word in data2 for word in neg):
     print('neg')
elif any(word in data2 for word in pos):
    print("pos")
'''
'''
count the  number of occurences of words in pos with reviews
'''
