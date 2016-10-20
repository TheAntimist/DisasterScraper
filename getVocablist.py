

def getVocablist():
    target = open('/home/emanon/Desktop/Kludge/vocablist.txt', 'r')
    words = target.readlines()
    vclist = []

    for word in words:
        word = word.strip()
        vclist.append(word)

    return vclist
