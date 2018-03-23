import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy


def format_sentence(sent):
    return {word: True for word in nltk.word_tokenize(sent)}


pos = []
with open("rt-polarity.pos.txt") as p:
    for words in p:
        pos.append([format_sentence(words), 'pos'])

neg = []
with open("rt-polarity.neg.txt") as p:
    for words in p:
        neg.append([format_sentence(words), 'neg'])

training = pos[:int((.8) * len(pos))] + neg[:int((.8) * len(neg))]
test = pos[int((.8) * len(pos)):] + neg[int((.8) * len(neg)):]

classifier = NaiveBayesClassifier.train(training)
#Replace here!
''' 
test pos
'''

example1 = "virtuoso achievement by Mr. Guadagnino."
example2 = "Anyone who has had -- or has imagined -- a doomed youthful fling " \
           "might be susceptible to this charming, bittersweet film."
example3 = "Michael Stuhlbarg gives a strong supporting performance as " \
           "Elio's compassionate father and Hammer is very well-cast, but " \
           "Chalamet owns the film with his passionate ambiguity."
example4 = "is extraordinarily beautiful cinematically, technically and " \
           "artistically. All performances are exceptional. With a poignant story " \
           "of the disappointment and exhilaration springing from the uncertainty of " \
           "any young love, the story and characters "
example5 = "Although it is not always subtle and can be a bit repetitious " \
           "sometimes, this is a touching coming-of-age drama that benefits " \
           "from an excellent performance by Timothée Chalamet (a revelation) " \
           "and understands so well the insecurities and anguish that come with first "
'''
test neg 
'''
example6 = "If you don't think too hard about why Neeson gets brought \
           in or how the baddies operate or what the point is, you may" \
           " be able to enjoy yourself. At least until the final act, when" \
           " the film goes off the rails. Like a train might do."
example7 = "This clumsily orchestrated and preposterously plotted film" \
           " judders to a standstill long before that speeding train does."
example8 = "The Hitchcockian stranger-on-a-train premise is squandered on " \
           "lapses in logic and generic close-combat skirmishes. Slow-motion " \
           "shots and endless tracking through the compartments further impede the " \
           "flow of a deadly-dull narrative"
example9 = "The movie is half-baked, incoherent and frequently dull (a key plot point hinges " \
           "on the difference between a daily or a weekly travel pass), yet, astoundingly, it is set up for a sequel."
example10 = "Liam Neeson has been bedeviled on an airplane. He's been bedeviled on a train. " \
            "At this point, Neeson is going to find trouble on every form of public transportation. " \
            "The Commuter is the fourth collaboration between America's favorite geriatric action star and director "

print("expected value for 1-5: pos....test value: ")

print(classifier.classify(format_sentence(example1)) + " 1")
print(classifier.classify(format_sentence(example2)) + " 2")
print(classifier.classify(format_sentence(example3)) + " 3")
print(classifier.classify(format_sentence(example4)) + " 4")
print(classifier.classify(format_sentence(example5)) + " 5")

print("expected value for 6-10: neg...test value: ")

print(classifier.classify(format_sentence(example6)) + " 6")
print(classifier.classify(format_sentence(example7)) + " 7")
print(classifier.classify(format_sentence(example8)) + " 8")
print(classifier.classify(format_sentence(example9)) + " 9")
print(classifier.classify(format_sentence(example10)) + " 10")


#larger-tests-pos


examplePos = open("posRevTest").read()

#larger-tests-neg

exampleNeg = open("negRevTest").read()

print("expected value: pos.... test value:")
print(classifier.classify(format_sentence(examplePos)))
print("expected value: neg.... test value:")
print(classifier.classify(format_sentence(exampleNeg)))


print('predicted accuracy:')

print(accuracy(classifier, test))

classifier.show_most_informative_features()
'''
print("actual accuracy:")
print("100%")
'''