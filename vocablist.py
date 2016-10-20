import os
from stemming.porter2 import stem
# import sys
# sys.path.append('/home/emanon/Desktop/Kludge/Python Code/')

from collections import Counter
from cleanhtml import clean_html
import nltk

c, directory = Counter(), '/home/emanon/Desktop/Kludge/Dataset/disaster/'

for x in os.listdir(directory):
    fname = os.path.join(directory, x)
    if os.path.isfile(fname):
        with open(fname) as f:
            cleaned = stem(clean_html(f.read().replace('\n', ' ')))
            c += Counter(nltk.word_tokenize(cleaned))


directory = '/home/emanon/Desktop/Kludge/Dataset/not/'

for x in os.listdir(directory):
    fname = os.path.join(directory, x)
    if os.path.isfile(fname):
        with open(fname) as f:
            cleaned = stem(clean_html(f.read().replace('\n', ' ')))
            c += Counter(nltk.word_tokenize(cleaned))


vclist = []
threshold = 50

for word in c:
    if c[word] >= threshold:
        vclist.append(word)
        print word, c[word]

vclist.sort()
target = open('/home/emanon/Desktop/Kludge/vocablist.txt', 'w')
target.truncate()

for word in vclist:
    target.write(word + '\n')

target.close()
