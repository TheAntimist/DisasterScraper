import cPickle
from sklearn import svm
import numpy

def predict(html):
    with open('/home/emanon/Desktop/Kludge/class.pkl', 'rb') as fid:
    clf = cPickle.load(fid)
    nx = numpy.zeros((1,len(vlist)))
    cleaned = stem(clean_html(html))
    ftok = nltk.word_tokenize(cleaned)
    word_indices = getwordindices(ftok, vlist)
    for index in word_indices:
        nx[0,index] = 1
    return clf.predict(nx)

    
