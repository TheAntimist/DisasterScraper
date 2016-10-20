import numpy
from stemming.porter2 import stem
import sys
sys.path.append('/home/emanon/Desktop/Kludge/Python Code/')

import getVocablist
from cleanhtml import clean_html
from getVocablist import *
import nltk

def getwordindices(cleaned, vocablist):
    wi = []
    
    for token in cleaned:
        if token in vocablist:
            wi.append(vocablist.index(token))
            # Actual index is vocablist + 1, because of Python using 0 indexing

    return wi



vlist = getVocablist()
directory = '/home/emanon/Desktop/Kludge/Dataset/disaster'
d = os.listdir(directory)
d_not = os.listdir('/home/emanon/Desktop/Kludge/Dataset/not')

X = numpy.zeros((len(d) + len(d_not), len(vlist)))
y = numpy.zeros((len(d) + len(d_not), ))

i = 0;

for x in d:
    fname = os.path.join(directory, x)
    if os.path.isfile(fname):
        with open(fname) as f:
            cleaned = stem(clean_html(f.read().replace('\n', ' ')))
            ftok = nltk.word_tokenize(cleaned)
            word_indices = getwordindices(ftok, vlist)
            for index in word_indices:
                X[i, index] = 1
              
            y[i] = 1
            i = i + 1
            

directory = '/home/emanon/Desktop/Kludge/Dataset/not'
d = d_not

for x in d:
    fname = os.path.join(directory, x)
    if os.path.isfile(fname):
        with open(fname) as f:
            cleaned = stem(clean_html(f.read().replace('\n', ' ')))
            ftok = nltk.word_tokenize(cleaned)
            word_indices = getwordindices(ftok,vlist)
            for index in word_indices:
                X[i, index] = 1
            i = i + 1
